import concurrent
from functools import partial

import pandas as pd
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import JsonResponse

from .models import Job
from .serializers import JobSerializer
from rest_framework import generics

from .processing.data_handler import save_dataframe_to_db
from .processing.preprocessing import preprocess_job
from .processing.related_keywords_handler import train_keyword_model, find_related_keywords
from .processing.requirements_handler import calculate_requirements
from .scrapers.linkedin import get_jobs_for_keyword


@login_required
def saml_auth(request):
    user_data = {
        'id': request.user.id,
        'username': request.user.username,
        'email': request.user.email,
        'first_name': request.user.first_name,
        'last_name': request.user.last_name,
    }
    return JsonResponse(user_data)


# @login_required
class JobList(generics.ListCreateAPIView):
    serializer_class = JobSerializer

    def get_queryset(self):

        query = self.request.query_params.get('search', '')
        query = str(query).replace(' ', '%20').lower()
        location = "Israel"

        dataset = pd.DataFrame(columns=['title', 'company', 'location', 'description', 'url'])

        try:
            with concurrent.futures.ProcessPoolExecutor(max_workers=1) as executor:
                func = partial(get_jobs_for_keyword, location=location)
                results = list(executor.map(func, query))

            for df in results:
                if not df.empty:
                    dataset = pd.concat([dataset, df], axis=0, ignore_index=True)

            dataset = dataset.drop_duplicates()
            dataset = dataset.reset_index(drop=True)

        except Exception as e:
            print(f"An error occurred: {e}")

        if not dataset.empty:
            # preprocessing
            dataset['description'] = dataset['description'].apply(preprocess_job)
            dataset['title'] = dataset['title'].apply(preprocess_job)

            # model training
            dataset['title_and_description'] = dataset['title'] + ' ' + dataset['description']
            model, cluster_keywords, vectorizer = train_keyword_model(dataset['title_and_description'].tolist())

            # Add related keywords column based on trained model
            dataset['related_keywords'] = dataset['title'].apply(
                lambda job_title: find_related_keywords(job_title, model, cluster_keywords, vectorizer))

            # add requirements column based on NLP
            dataset = calculate_requirements(dataset)

            # save new data to db
            dataset = dataset.drop_duplicates()
            dataset = dataset.reset_index(drop=True)
            save_dataframe_to_db(dataset)

        # Search for user keywords in entire db
        queryset = Job.objects.filter(
            Q(title__icontains=query) |
            Q(company__icontains=query) |
            Q(location__icontains=query) |
            Q(description__icontains=query) |
            Q(requirements__icontains=query) |
            Q(related_keywords__icontains=query)
        )
        return queryset
