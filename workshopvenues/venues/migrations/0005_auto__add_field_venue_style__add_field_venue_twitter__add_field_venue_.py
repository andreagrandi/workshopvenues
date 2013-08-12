# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Venue.style'
        db.add_column(u'venues_venue', 'style',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=200, blank=True),
                      keep_default=False)

        # Adding field 'Venue.twitter'
        db.add_column(u'venues_venue', 'twitter',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=200, blank=True),
                      keep_default=False)

        # Adding field 'Venue.phone'
        db.add_column(u'venues_venue', 'phone',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=30, blank=True),
                      keep_default=False)

        # Adding field 'Venue.contact'
        db.add_column(u'venues_venue', 'contact',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=50, blank=True),
                      keep_default=False)

        # Adding field 'Venue.contact_email'
        db.add_column(u'venues_venue', 'contact_email',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=50, blank=True),
                      keep_default=False)

        # Adding field 'Venue.contact_twitter'
        db.add_column(u'venues_venue', 'contact_twitter',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=200, blank=True),
                      keep_default=False)

        # Adding field 'Venue.cost'
        db.add_column(u'venues_venue', 'cost',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=200, blank=True),
                      keep_default=False)

        # Adding field 'Venue.capacity'
        db.add_column(u'venues_venue', 'capacity',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=200, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Venue.style'
        db.delete_column(u'venues_venue', 'style')

        # Deleting field 'Venue.twitter'
        db.delete_column(u'venues_venue', 'twitter')

        # Deleting field 'Venue.phone'
        db.delete_column(u'venues_venue', 'phone')

        # Deleting field 'Venue.contact'
        db.delete_column(u'venues_venue', 'contact')

        # Deleting field 'Venue.contact_email'
        db.delete_column(u'venues_venue', 'contact_email')

        # Deleting field 'Venue.contact_twitter'
        db.delete_column(u'venues_venue', 'contact_twitter')

        # Deleting field 'Venue.cost'
        db.delete_column(u'venues_venue', 'cost')

        # Deleting field 'Venue.capacity'
        db.delete_column(u'venues_venue', 'capacity')


    models = {
        u'venues.address': {
            'Meta': {'object_name': 'Address'},
            'country': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'postcode': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'town': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'venues.facility': {
            'Meta': {'object_name': 'Facility'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'venues.venue': {
            'Meta': {'object_name': 'Venue'},
            'address': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['venues.Address']"}),
            'capacity': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'contact': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'contact_email': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'contact_twitter': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'cost': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'facilities': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['venues.Facility']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'style': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'twitter': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'website': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['venues']