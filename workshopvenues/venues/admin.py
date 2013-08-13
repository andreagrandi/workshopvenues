from django.contrib import admin
from venues.models import Venue, Address, Facility, Image

admin.site.register(Venue)
admin.site.register(Address)
admin.site.register(Facility)
admin.site.register(Image)
