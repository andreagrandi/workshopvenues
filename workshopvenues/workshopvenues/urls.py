from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from venues import views as venues_views
from contact import views as contact_views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'workshopvenues.views.home', name='home'),
    # url(r'^workshopvenues/', include('workshopvenues.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', include('venues.urls')),
    url(r'^about/', venues_views.about, name='about'),
    url(r'^contact/', contact_views.contact, name='contact'),
    url(r'^venues/', include('venues.urls')),
)
