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
    website = models.CharField(max_length=50)
    address = models.ForeignKey(Address)
    facilities = models.ManyToManyField(Facility)

    def __unicode__(self):
        return self.name
