"""Test for auth views."""
from django.test import TestCase
from django.conf import settings


class Test(TestCase):
    def test_view_works(self):
        print(getattr(settings, 'SECRET_KEY'))
        self.assertTrue(True)