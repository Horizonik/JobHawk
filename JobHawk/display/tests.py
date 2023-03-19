import unittest

from django.test import TestCase
from django.urls import reverse
from .models import Job, Company


class JobViewTests(TestCase):
    def setUp(self):
        self.company = Company.objects.create(name='HorizonCorp', description='Ofeks company', founding_date='2018-01-01')
        self.job = Job.objects.create(title='Test Job', location='Israel', description='Bruh this is a test',
                                      requirements='Be a good programmer', date_published='2020-02-20',
                                      company=self.company)

    @unittest.expectedFailure
    def test_views(self):
        views = ['MainPageView', 'SearchPageView']
        for view_name in views:
            # Test for cross-site scripting (XSS) vulnerability
            response = self.client.get(reverse(view_name), {'search': '<script>alert("XSS")</script>'})
            self.assertNotContains(response, '<script>alert("XSS")</script>')

            # Test for SQL injection vulnerability
            search_term = "'; DROP TABLE JobHawk_Job;"
            response = self.client.get(reverse(view_name), {'search': search_term})
            self.assertNotContains(response, search_term)

            # Test for insecure direct object references vulnerability
            response = self.client.get(reverse(view_name, args=[self.job.id]))
            self.assertEqual(response.status_code, 200)

    def tearDown(self):
        self.company.delete()
        self.job.delete()
