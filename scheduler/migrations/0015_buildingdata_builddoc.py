# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-30 08:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0014_sysventefficiency'),
    ]

    operations = [
        migrations.AddField(
            model_name='buildingdata',
            name='builddoc',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='scheduler.BuildingDoc'),
            preserve_default=False,
        ),
    ]