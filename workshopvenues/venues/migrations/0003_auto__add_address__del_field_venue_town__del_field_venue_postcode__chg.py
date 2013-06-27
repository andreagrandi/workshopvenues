# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Address'
        db.create_table(u'venues_address', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('street', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('town', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('postcode', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal(u'venues', ['Address'])

        # Deleting field 'Venue.town'
        db.delete_column(u'venues_venue', 'town')

        # Deleting field 'Venue.postcode'
        db.delete_column(u'venues_venue', 'postcode')


        # Renaming column for 'Venue.address' to match new field type.
        db.rename_column(u'venues_venue', 'address', 'address_id')
        # Changing field 'Venue.address'
        db.alter_column(u'venues_venue', 'address_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['venues.Address']))
        # Adding index on 'Venue', fields ['address']
        db.create_index(u'venues_venue', ['address_id'])


    def backwards(self, orm):
        # Removing index on 'Venue', fields ['address']
        db.delete_index(u'venues_venue', ['address_id'])

        # Deleting model 'Address'
        db.delete_table(u'venues_address')

        # Adding field 'Venue.town'
        db.add_column(u'venues_venue', 'town',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=30),
                      keep_default=False)

        # Adding field 'Venue.postcode'
        db.add_column(u'venues_venue', 'postcode',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=10),
                      keep_default=False)


        # Renaming column for 'Venue.address' to match new field type.
        db.rename_column(u'venues_venue', 'address_id', 'address')
        # Changing field 'Venue.address'
        db.alter_column(u'venues_venue', 'address', self.gf('django.db.models.fields.CharField')(max_length=200))

    models = {
        u'venues.address': {
            'Meta': {'object_name': 'Address'},
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
            'facilities': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['venues.Facility']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'website': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['venues']