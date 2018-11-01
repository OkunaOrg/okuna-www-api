from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class TestHealth(APITestCase):
    """
    Health API
    """

    url = reverse('health')

    def test_should_say_hello(self):
        response = self.client.get(self.url)
        self.assertTrue(response.status_code, status.HTTP_200_OK)
