"""Test for auth views."""
from django.test import TestCase
from django.urls import reverse


class Test(TestCase):
    def test_view_works(self):
        url = reverse('user-list')

        response = self.client.post(url)

        print(response.data)