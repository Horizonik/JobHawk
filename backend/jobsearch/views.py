from django.contrib.auth.decorators import login_required
from rest_framework import generics, filters
from .models import Job
from .serializers import JobSerializer
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required


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


class JobList(generics.ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'description', 'company', 'location']
