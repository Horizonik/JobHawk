from django.urls import path
from . import views
from .views import saml_auth

urlpatterns = [
    path('jobs/', views.JobList.as_view(), name='job-list'),
    path('saml-auth/', saml_auth),
]
