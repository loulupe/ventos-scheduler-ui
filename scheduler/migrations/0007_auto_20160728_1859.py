# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-28 18:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0006_auto_20160728_1555'),
    ]

    operations = [
        migrations.AddField(
            model_name='buildingdoc',
            name='name',
            field=models.CharField(default='test', max_length=80),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='regdoc',
            name='name',
            field=models.CharField(default='test', max_length=80),
            preserve_default=False,
        ),
    ]
