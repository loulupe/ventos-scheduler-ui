# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-28 15:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0005_buildingdata_typeroom'),
    ]

    operations = [
        migrations.CreateModel(
            name='BuildingDoc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('docfile', models.FileField(upload_to='buildingDocs/%Y/%m/%d')),
            ],
        ),
        migrations.CreateModel(
            name='RegDoc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('docfile', models.FileField(upload_to='registrationDocs/%Y/%m/%d')),
            ],
        ),
        migrations.DeleteModel(
            name='Document',
        ),
        migrations.AddField(
            model_name='registration',
            name='relatedBuild',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]