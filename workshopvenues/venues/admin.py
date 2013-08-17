from django.contrib import admin
from venues.models import Venue, Facility, Image, Country

admin.site.register(Venue)
admin.site.register(Facility)
admin.site.register(Image)
admin.site.register(Country)
