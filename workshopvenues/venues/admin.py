from django.contrib import admin
from venues.models import Venue, Address, Facility

admin.site.register(Venue)
admin.site.register(Address)
admin.site.register(Facility)
