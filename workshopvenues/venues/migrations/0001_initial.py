# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name_plural': 'cities',
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name_plural': 'countries',
            },
        ),
        migrations.CreateModel(
            name='Facility',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name_plural': 'facilities',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('filename', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('website', models.CharField(max_length=50, null=True, blank=True)),
                ('address', models.CharField(max_length=200, null=True, blank=True)),
                ('postcode', models.CharField(max_length=10, null=True, blank=True)),
                ('style', models.CharField(max_length=200, null=True, blank=True)),
                ('twitter', models.CharField(max_length=200, null=True, blank=True)),
                ('phone', models.CharField(max_length=30, null=True, blank=True)),
                ('contact', models.CharField(max_length=50, null=True, blank=True)),
                ('contact_email', models.CharField(max_length=50, null=True, blank=True)),
                ('contact_twitter', models.CharField(max_length=200, null=True, blank=True)),
                ('cost', models.CharField(max_length=200, null=True, blank=True)),
                ('capacity', models.CharField(max_length=200, null=True, blank=True)),
                ('active', models.BooleanField()),
                ('city', models.ForeignKey(blank=True, to='venues.City', null=True)),
                ('country', models.ForeignKey(blank=True, to='venues.Country', null=True)),
                ('facilities', models.ManyToManyField(to='venues.Facility', null=True, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='image',
            name='venue',
            field=models.ForeignKey(to='venues.Venue'),
        ),
        migrations.AddField(
            model_name='city',
            name='country',
            field=models.ForeignKey(to='venues.Country'),
        ),
    ]
