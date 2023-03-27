"""component that converts Django models to JSON objects and vice-versa"""

from rest_framework import serializers
from .models import Job


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ('id', 'title', 'company', 'location', 'description', 'requirements', 'related_keywords', 'url')