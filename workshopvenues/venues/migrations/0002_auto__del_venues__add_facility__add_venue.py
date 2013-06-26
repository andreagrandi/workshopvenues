# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Venues'
        db.delete_table(u'venues_venues')

        # Adding model 'Facility'
        db.create_table(u'venues_facility', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'venues', ['Facility'])

        # Adding model 'Venue'
        db.create_table(u'venues_venue', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('website', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('town', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('postcode', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal(u'venues', ['Venue'])

        # Adding M2M table for field facilities on 'Venue'
        m2m_table_name = db.shorten_name(u'venues_venue_facilities')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('venue', models.ForeignKey(orm[u'venues.venue'], null=False)),
            ('facility', models.ForeignKey(orm[u'venues.facility'], null=False))
        ))
        db.create_unique(m2m_table_name, ['venue_id', 'facility_id'])


    def backwards(self, orm):
        # Adding model 'Venues'
        db.create_table(u'venues_venues', (
            ('town', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('website', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('postcode', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=200)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'venues', ['Venues'])

        # Deleting model 'Facility'
        db.delete_table(u'venues_facility')

        # Deleting model 'Venue'
        db.delete_table(u'venues_venue')

        # Removing M2M table for field facilities on 'Venue'
        db.delete_table(db.shorten_name(u'venues_venue_facilities'))


    models = {
        u'venues.facility': {
            'Meta': {'object_name': 'Facility'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'venues.venue': {
            'Meta': {'object_name': 'Venue'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'facilities': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['venues.Facility']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'postcode': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'town': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'website': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['venues']