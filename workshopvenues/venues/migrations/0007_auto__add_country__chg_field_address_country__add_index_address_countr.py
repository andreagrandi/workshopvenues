# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Country'
        db.create_table(u'venues_country', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'venues', ['Country'])

        # Deleting field 'Address.country'
        db.delete_column(u'venues_address', 'country')


    def backwards(self, orm):
        # Deleting model 'Country'
        db.delete_table(u'venues_country')

        # Adding field 'Address.country'
        db.add_column(u'venues_address', 'country',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=30, blank=True),
                      keep_default=False)


    models = {
        u'venues.address': {
            'Meta': {'object_name': 'Address'},
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
            'website': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'})
        }
    }

    complete_apps = ['venues']