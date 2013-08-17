"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from .models import Address, Venue, Facility, Image, Country


class ModelsTest(TestCase):
    def test_create_address(self):
        c = Country()
        c.name = "United Kingdom"
        c.save()
        a = Address()
        a.street = '23, Test Street'
        a.town = 'London'
        a.postcode = 'xxxxx'
        a.country = c
        a.save()
        self.assertTrue(a.id >= 0)

    def test_create_facility(self):
        fac_wifi = Facility()
        fac_wifi.name = 'WiFi'
        fac_wifi.save()
        self.assertTrue(fac_wifi.id >= 0)

        fac_elevator = Facility()
        fac_elevator.name = 'Elevator'
        fac_elevator.save()
        self.assertTrue(fac_elevator.id >= 0)

    def test_create_venue(self):
        # Create the Country
        c = Country()
        c.name = "United Kingdom"
        c.save()

        # Create the address first
        a = Address()
        a.street = '23, Test Street'
        a.town = 'London'
        a.postcode = 'xxxxx'
        a.country = c
        a.save()

        fac_wifi = Facility()
        fac_wifi.name = 'WiFi'
        fac_wifi.save()
        self.assertTrue(fac_wifi.id >= 0)

        fac_elevator = Facility()
        fac_elevator.name = 'Elevator'
        fac_elevator.save()
        self.assertTrue(fac_elevator.id >= 0)

        # Create the venue
        v = Venue()
        v.name = 'Venue Test'
        v.website = 'www.myvenue.com'
        v.address = a
        v.save()
        v.facilities.add(fac_wifi)
        v.facilities.add(fac_elevator)
        self.assertEqual(v.address.town, 'London')
        self.assertTrue(v.id >= 0)
    
    def test_create_image(self):
        # Create the Country
        c = Country()
        c.name = "United Kingdom"
        c.save()

        # Create the address first
        a = Address()
        a.street = '23, Test Street'
        a.town = 'London'
        a.postcode = 'xxxxx'
        a.country = c
        a.save()  
        
        fac_wifi = Facility()
        fac_wifi.name = 'WiFi'
        fac_wifi.save()
        self.assertTrue(fac_wifi.id >= 0)

        fac_elevator = Facility()
        fac_elevator.name = 'Elevator'
        fac_elevator.save()
        self.assertTrue(fac_elevator.id >= 0)
              
        # Create the Venue 
        v = Venue()
        v.name = 'Venue Test'
        v.website = 'www.myvenue.com'
        v.address = a
        v.save() 
        v.facilities.add(fac_wifi)
        v.facilities.add(fac_elevator)
        
        # Create the image
        i = Image()
        i.filename = '/test/image/path'
        i.venue = v
        i.save()
        self.assertEqual(i.venue.name, 'Venue Test')        
        self.assertTrue(i.id >= 0) 
