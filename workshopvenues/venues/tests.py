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

class VenueFactory(factory.DjangoModelFactory):
    FACTORY_FOR = Venue
    country = factory.SubFactory(CountryFactory)
    city = factory.SubFactory(CityFactory)
    name = 'Vanue Test'
    website = 'www.myvenue.com'
    address = '23, Test Street'
    postcode = 'xxxxx'
    active = True

    @factory.post_generation
    def facilities(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of facilities were passed in, use them
            for facility in extracted:
                self.facilities.add(facility)

class ImageFactory(factory.DjangoModelFactory):
    FACTORY_FOR = Image
    venue = factory.SubFactory(VenueFactory)
    filename = 'image001.jpg'

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
        venue = VenueFactory.create(facilities = (FacilityFactory(name = 'WiFI'), 
            FacilityFactory.create(name = 'Elevator')))
        self.assertTrue(venue.id >= 0)
    
    def test_create_image(self):
        image = ImageFactory.create()        
        self.assertTrue(image.id >= 0) 
