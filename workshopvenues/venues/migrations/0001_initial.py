# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Venues'
        db.create_table(u'venues_venues', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('website', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('town', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('postcode', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal(u'venues', ['Venues'])


    def backwards(self, orm):
        # Deleting model 'Venues'
        db.delete_table(u'venues_venues')


    models = {
        u'venues.venues': {
            'Meta': {'object_name': 'Venues'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'postcode': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'town': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'website': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['venues']