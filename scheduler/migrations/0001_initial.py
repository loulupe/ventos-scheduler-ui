# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-26 16:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AirDistConf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('configuration', models.CharField(max_length=255)),
                ('value', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='BuildingData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('building', models.CharField(max_length=70)),
                ('room', models.BigIntegerField()),
                ('facilityId', models.CharField(max_length=70)),
                ('capacity', models.PositiveIntegerField()),
                ('acadOrg', models.CharField(max_length=20)),
                ('area', models.PositiveIntegerField()),
                ('maxOccupant', models.PositiveIntegerField()),
                ('roomName', models.CharField(max_length=70)),
                ('spaceCategory', models.CharField(max_length=70)),
                ('system', models.CharField(max_length=10)),
                ('vav', models.CharField(max_length=20)),
                ('indUnit', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('term', models.IntegerField()),
                ('session', models.IntegerField()),
                ('acadGroup', models.CharField(max_length=10)),
                ('subject', models.CharField(max_length=10)),
                ('catalog', models.IntegerField()),
                ('sectionComponent', models.CharField(max_length=255)),
                ('descr', models.CharField(max_length=255)),
                ('classNbr', models.IntegerField()),
                ('campus', models.CharField(max_length=255)),
                ('totEnrl', models.IntegerField()),
                ('facilID', models.CharField(max_length=255)),
                ('mtgStart', models.DateTimeField()),
                ('MtgEnd', models.DateTimeField()),
                ('mon', models.BooleanField()),
                ('tues', models.BooleanField()),
                ('wed', models.BooleanField()),
                ('thurs', models.BooleanField()),
                ('fri', models.BooleanField()),
                ('sat', models.BooleanField()),
                ('sun', models.BooleanField()),
                ('startDate', models.DateTimeField()),
                ('endDate', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='VentRate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spaceCategory', models.CharField(max_length=70)),
                ('airRatePerson', models.IntegerField()),
                ('airRateArea', models.IntegerField()),
            ],
        ),
    ]