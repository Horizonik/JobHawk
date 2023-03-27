from django.db import models


class Job(models.Model):
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    location = models.CharField(max_length=80)

    description = models.TextField(max_length=600)
    requirements = models.CharField(max_length=200)
    related_keywords = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    # date_published = models.DateTimeField('Published')

    def __str__(self):
        return self.title
