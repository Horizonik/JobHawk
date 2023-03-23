from django.urls import path
from . import views

urlpatterns = [
    path('jobs/', views.JobList.as_view(), name='job-list'),
]