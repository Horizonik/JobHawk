from django.urls import path

from .views import MainPageView, SearchPageView

urlpatterns = [
    path('', MainPageView.as_view(), name="home"),
    path('search', SearchPageView.as_view(), name="search_results"),
]