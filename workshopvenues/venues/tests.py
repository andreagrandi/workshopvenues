"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
import factory
from .models import Venue, Facility, Image, Country, City

class FacilityFactory(factory.DjangoModelFactory):
    FACTORY_FOR = Facility

class CountryFactory(factory.DjangoModelFactory):
    FACTORY_FOR = Country

class CityFactory(factory.DjangoModelFactory):
    FACTORY_FOR = City
    country = factory.SubFactory(CountryFactory)

class ModelsTest(TestCase):
    def test_create_facility(self):
        fac_wifi = FacilityFactory.create(name = 'WiFi')
        self.assertTrue(fac_wifi.id >= 0)

        fac_elevator = FacilityFactory.create(name = 'Elevator')
        self.assertTrue(fac_elevator.id >= 0)

    def test_create_country(self):
        country = CountryFactory.create(name = 'United Kingdom')
        self.assertTrue(country.id >= 0)

    def test_create_city(self):
        # Create the City
        city = CityFactory.create(name = 'London')
        self.assertTrue(city.id >= 0)

    def test_create_venue(self):
        # Create the Country first
        country = Country()
        country.name = "United Kingdom"
        country.save()

        # Create the City
        city = City()
        city.name = "London"
        city.country = country
        city.save()
        self.assertTrue(city.id >= 0)

        # Create facilities
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
        v.street = '23, Test Street'
        v.postcode = 'xxxxx'
        v.country = country
        v.city = city
        v.active = True
        v.save()
        v.facilities.add(fac_wifi)
        v.facilities.add(fac_elevator)
        self.assertEqual(v.city.name, 'London')
        self.assertEqual(v.country.name, 'United Kingdom')
        self.assertTrue(v.id >= 0)
    
    def test_create_image(self):
        # Create the Country first
        country = Country()
        country.name = "United Kingdom"
        country.save()

        # Create the City
        city = City()
        city.name = "London"
        city.country = country
        city.save()
        self.assertTrue(city.id >= 0)

        # Create facilities
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
        v.street = '23, Test Street'
        v.postcode = 'xxxxx'
        v.country = country
        v.city = city
        v.active = True
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
