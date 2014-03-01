"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "./manage.py test --settings=workshopvenues.settings_test venues"

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from .factories import FacilityFactory, CountryFactory, CityFactory, VenueFactory, ImageFactory

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

    def test_build_venue(self):
        venue = VenueFactory.build(facilities = (FacilityFactory(name = 'WiFI'), 
            FacilityFactory.build(name = 'Elevator')))
        self.assertEqual(venue.id, None, "Venue id is None when is not saved.")
    
    def test_create_image(self):
        image = ImageFactory.create()        
        self.assertTrue(image.id >= 0) 
