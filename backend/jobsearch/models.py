from django.db import models


class Job(models.Model):
    title = models.CharField(max_length=60)
    company = models.CharField(max_length=50)
    location = models.CharField(max_length=80)

    description = models.TextField(max_length=1500)
    requirements = models.CharField(max_length=500)
    related_keywords = models.CharField(max_length=500)
    url = models.CharField(max_length=500)

    def __str__(self):
        return self.title
