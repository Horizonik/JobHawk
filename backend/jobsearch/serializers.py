"""component that converts Django models to JSON objects and vice-versa"""

from rest_framework import serializers
from .models import Job, Company


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ('id', 'title', 'requirements', 'date_published', 'company')


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('id', 'name', 'founding_date')