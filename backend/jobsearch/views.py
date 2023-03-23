from django.shortcuts import render
from rest_framework import generics, filters
from .models import Job
from .serializers import JobSerializer


class JobList(generics.ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'description', 'company', 'location']
