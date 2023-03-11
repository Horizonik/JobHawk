from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView, TemplateView

from .forms import SearchForm
from .models import Job


class MainPage(TemplateView):
    template_name = 'display/main_page.html'


class SearchPage(ListView):
    model = Job
    template_name = 'display/search_page.html'
