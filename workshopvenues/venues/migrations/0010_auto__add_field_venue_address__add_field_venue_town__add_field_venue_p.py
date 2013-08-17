# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Venue.address'
        db.add_column(u'venues_venue', 'address',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=200, blank=True),
                      keep_default=False)

        # Adding field 'Venue.town'
        db.add_column(u'venues_venue', 'town',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=30, blank=True),
                      keep_default=False)

        # Adding field 'Venue.postcode'
        db.add_column(u'venues_venue', 'postcode',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=10, blank=True),
                      keep_default=False)

        # Adding field 'Venue.country'
        db.add_column(u'venues_venue', 'country',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['venues.Country'], null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Venue.address'
        db.delete_column(u'venues_venue', 'address')

        # Deleting field 'Venue.town'
        db.delete_column(u'venues_venue', 'town')

        # Deleting field 'Venue.postcode'
        db.delete_column(u'venues_venue', 'postcode')

        # Deleting field 'Venue.country'
        db.delete_column(u'venues_venue', 'country_id')


    models = {
        u'venues.address': {
            'Meta': {'object_name': 'Address'},
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['venues.Country']", 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'postcode': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'town': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'venues.country': {
            'Meta': {'object_name': 'Country'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'venues.facility': {
            'Meta': {'object_name': 'Facility'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'venues.image': {
            'Meta': {'object_name': 'Image'},
            'filename': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'venue': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['venues.Venue']"})
        },
        u'venues.venue': {
            'Meta': {'object_name': 'Venue'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'capacity': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'contact': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'contact_email': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'contact_twitter': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'cost': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['venues.Country']", 'null': 'True'}),
            'facilities': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['venues.Facility']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'postcode': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'style': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'town': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'twitter': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'website': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'})
        }
    }

    complete_apps = ['venues']