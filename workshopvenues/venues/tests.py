"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from .models import Address


class ModelsTest(TestCase):
    def test_create_address(self):
        a = Address()
        a.street = '23, Test Street'
        a.town = 'London'
        a.postcode = 'xxxxx'
        a.country = 'UK'
        a.save()
        self.assertTrue(a.id >= 0)
