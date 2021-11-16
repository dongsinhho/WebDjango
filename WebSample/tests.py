from django.http import response
from django.test import TestCase, SimpleTestCase

# Create your tests here.

class SimpleTests(SimpleTestCase):
    def test_home_page_status(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)
    def test_details_page_status(self):
        response = self.client.get('/details/')
        self.assertEquals(response.status_code, 200)
    def test_profile_page_status(self):
        response = self.client.get('/profile/')
        self.assertEquals(response.status_code, 200)