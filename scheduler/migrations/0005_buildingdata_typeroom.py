# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-28 09:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0004_auto_20160727_1211'),
    ]

    operations = [
        migrations.AddField(
            model_name='buildingdata',
            name='typeRoom',
            field=models.CharField(default='', max_length=70),
            preserve_default=False,
        ),
    ]
