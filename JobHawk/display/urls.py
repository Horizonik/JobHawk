from django.urls import path

from .views import MainPageView, SearchPageView

urlpatterns = [
    path('', MainPageView.as_view(), name="MainPageView"),
    path('search', SearchPageView.as_view(), name="SearchPageView"),
]