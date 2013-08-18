# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Venue.website'
        db.alter_column(u'venues_venue', 'website', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'Venue.style'
        db.alter_column(u'venues_venue', 'style', self.gf('django.db.models.fields.CharField')(max_length=200, null=True))

        # Changing field 'Venue.capacity'
        db.alter_column(u'venues_venue', 'capacity', self.gf('django.db.models.fields.CharField')(max_length=200, null=True))

        # Changing field 'Venue.twitter'
        db.alter_column(u'venues_venue', 'twitter', self.gf('django.db.models.fields.CharField')(max_length=200, null=True))

        # Changing field 'Venue.address'
        db.alter_column(u'venues_venue', 'address', self.gf('django.db.models.fields.CharField')(max_length=200, null=True))

        # Changing field 'Venue.contact'
        db.alter_column(u'venues_venue', 'contact', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'Venue.phone'
        db.alter_column(u'venues_venue', 'phone', self.gf('django.db.models.fields.CharField')(max_length=30, null=True))

        # Changing field 'Venue.cost'
        db.alter_column(u'venues_venue', 'cost', self.gf('django.db.models.fields.CharField')(max_length=200, null=True))

        # Changing field 'Venue.contact_email'
        db.alter_column(u'venues_venue', 'contact_email', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'Venue.postcode'
        db.alter_column(u'venues_venue', 'postcode', self.gf('django.db.models.fields.CharField')(max_length=10, null=True))

        # Changing field 'Venue.contact_twitter'
        db.alter_column(u'venues_venue', 'contact_twitter', self.gf('django.db.models.fields.CharField')(max_length=200, null=True))

    def backwards(self, orm):

        # Changing field 'Venue.website'
        db.alter_column(u'venues_venue', 'website', self.gf('django.db.models.fields.CharField')(default='', max_length=50))

        # Changing field 'Venue.style'
        db.alter_column(u'venues_venue', 'style', self.gf('django.db.models.fields.CharField')(default='', max_length=200))

        # Changing field 'Venue.capacity'
        db.alter_column(u'venues_venue', 'capacity', self.gf('django.db.models.fields.CharField')(default='', max_length=200))

        # Changing field 'Venue.twitter'
        db.alter_column(u'venues_venue', 'twitter', self.gf('django.db.models.fields.CharField')(default='', max_length=200))

        # Changing field 'Venue.address'
        db.alter_column(u'venues_venue', 'address', self.gf('django.db.models.fields.CharField')(default='', max_length=200))

        # Changing field 'Venue.contact'
        db.alter_column(u'venues_venue', 'contact', self.gf('django.db.models.fields.CharField')(default='', max_length=50))

        # Changing field 'Venue.phone'
        db.alter_column(u'venues_venue', 'phone', self.gf('django.db.models.fields.CharField')(default='', max_length=30))

        # Changing field 'Venue.cost'
        db.alter_column(u'venues_venue', 'cost', self.gf('django.db.models.fields.CharField')(default='', max_length=200))

        # Changing field 'Venue.contact_email'
        db.alter_column(u'venues_venue', 'contact_email', self.gf('django.db.models.fields.CharField')(default='', max_length=50))

        # Changing field 'Venue.postcode'
        db.alter_column(u'venues_venue', 'postcode', self.gf('django.db.models.fields.CharField')(default='', max_length=10))

        # Changing field 'Venue.contact_twitter'
        db.alter_column(u'venues_venue', 'contact_twitter', self.gf('django.db.models.fields.CharField')(default='', max_length=200))

    models = {
        u'venues.city': {
            'Meta': {'object_name': 'City'},
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['venues.Country']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
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
            'address': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'capacity': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['venues.City']", 'null': 'True', 'blank': 'True'}),
            'contact': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'contact_email': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'contact_twitter': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'cost': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['venues.Country']", 'null': 'True', 'blank': 'True'}),
            'facilities': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['venues.Facility']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'postcode': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'style': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'twitter': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'website': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['venues']