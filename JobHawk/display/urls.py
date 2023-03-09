from django.urls import path

from .views import MainPage, SearchPage

urlpatterns = [
    path('', MainPage.as_view()),
    path('search', SearchPage.as_view()),
]