from django.db import models


class Job(models.Model):
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=80)
    description = models.TextField(max_length=200, default="-")
    requirements = models.CharField(max_length=200)
    date_published = models.DateTimeField('Published')
    company = models.CharField(max_length=100)

    def __str__(self):
        return self.title
