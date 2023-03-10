from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import View, TemplateView

from .forms import SearchForm


# Create your views here.
class MainPage(TemplateView):
    template_name = 'display/gpt.html'


class SearchPage(View):
    form_class = SearchForm
    initial = {'key': 'value'}
    template_name = 'display/search_page.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            return HttpResponseRedirect('/success/')

        return render(request, self.template_name, {'form': form})
