from django.utils.html import escape
from django.views.generic import ListView, TemplateView
from .models import Job


class MainPageView(TemplateView):
    template_name = 'display/main_page.html'


class SearchPageView(ListView):
    model = Job
    template_name = 'display/search_page.html'
    context_object_name = 'results'
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get('query')

        if query:
            query = escape(query)
            return Job.objects.filter(title__icontains=query).order_by('date_published')

        return Job.objects.none()
