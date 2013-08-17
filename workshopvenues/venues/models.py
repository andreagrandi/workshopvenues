from django.db import models

class Facility(models.Model):
    name = models.CharField(max_length=30)

    def __unicode__(self):
        return self.name

class Address(models.Model):
    street = models.CharField(max_length=200)
    town = models.CharField(max_length=30)
    postcode = models.CharField(max_length=10)
    country = models.CharField(max_length=30, blank=True)

class Venue(models.Model):
    name = models.CharField(max_length=30)
    website = models.CharField(max_length=50, blank=True)
    address = models.ForeignKey(Address)
    facilities = models.ManyToManyField(Facility)
    style = models.CharField(max_length=200, blank=True)
    twitter = models.CharField(max_length=200, blank=True)
    phone = models.CharField(max_length=30, blank=True)
    contact = models.CharField(max_length=50, blank=True)
    contact_email = models.CharField(max_length=50, blank=True)
    contact_twitter = models.CharField(max_length=200, blank=True)
    cost = models.CharField(max_length=200, blank=True)
    capacity = models.CharField(max_length=200, blank=True)

    def __unicode__(self):
        return self.name

class Image(models.Model):
    filename = models.CharField(max_length=255)
    venue = models.ForeignKey(Venue)

