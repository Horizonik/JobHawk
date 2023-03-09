from django.db import models


# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    founding_date = models.DateTimeField('Founded')

    def __str__(self):
        return self.name


class Job(models.Model):
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=80)
    description = models.TextField(max_length=200)
    requirements = models.CharField(max_length=1000)
    date_published = models.DateTimeField('Published')
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
