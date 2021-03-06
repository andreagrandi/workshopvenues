from django.db import models

class Facility(models.Model):
    name = models.CharField(max_length=30)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "facilities"

class Country(models.Model):
    name = models.CharField(max_length=30)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "countries"

class City(models.Model):
    name = models.CharField(max_length=30)
    country = models.ForeignKey(Country)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "cities"

class Venue(models.Model):
    name = models.CharField(max_length=50)
    website = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    city = models.ForeignKey(City, null=True, blank=True)
    postcode = models.CharField(max_length=10, blank=True, null=True)
    country = models.ForeignKey(Country, null=True, blank=True)
    facilities = models.ManyToManyField(Facility, null=True, blank=True)
    style = models.CharField(max_length=200, blank=True, null=True)
    twitter = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=30, blank=True, null=True)
    contact = models.CharField(max_length=50, blank=True, null=True)
    contact_email = models.CharField(max_length=50, blank=True, null=True)
    contact_twitter = models.CharField(max_length=200, blank=True, null=True)
    cost = models.CharField(max_length=200, blank=True, null=True)
    capacity = models.CharField(max_length=200, blank=True, null=True)
    active = models.BooleanField()

    def __unicode__(self):
        return self.name

class Image(models.Model):
    filename = models.CharField(max_length=255)
    venue = models.ForeignKey(Venue)
