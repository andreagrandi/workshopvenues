from django.contrib import admin
from venues.models import Venue, Address, Facility, Image, Country

admin.site.register(Venue)
admin.site.register(Address)
admin.site.register(Facility)
admin.site.register(Image)
admin.site.register(Country)
