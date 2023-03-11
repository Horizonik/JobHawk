from django.urls import path

from .views import MainPage, SearchPage

urlpatterns = [
    path('', MainPage.as_view(), name="home"),
    path('search', SearchPage.as_view(), name="search_results"),
]