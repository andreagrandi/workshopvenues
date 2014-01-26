import factory
from venues.models import Venue, Facility, Image, Country, City

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