# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-31 01:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0017_auto_20160731_0006'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='status',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]