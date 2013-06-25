from django.db import models

class Venues(models.Model):
    name = models.CharField(max_length=30)
    website = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    town = models.CharField(max_length=30)
    postcode = models.CharField(max_length=10)

    def __unicode__(self):
        return self.name