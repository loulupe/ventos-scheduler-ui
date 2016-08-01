# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-31 00:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0016_auto_20160731_0002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='airflow',
            name='areaSqft',
            field=models.DecimalField(decimal_places=2, max_digits=11),
        ),
        migrations.AlterField(
            model_name='airflow',
            name='ev',
            field=models.DecimalField(decimal_places=2, max_digits=11),
        ),
        migrations.AlterField(
            model_name='airflow',
            name='ez',
            field=models.DecimalField(decimal_places=2, max_digits=11),
        ),
        migrations.AlterField(
            model_name='airflow',
            name='idleDamperPosition',
            field=models.DecimalField(decimal_places=2, max_digits=11),
        ),
        migrations.AlterField(
            model_name='airflow',
            name='leed',
            field=models.DecimalField(decimal_places=2, max_digits=11),
        ),
        migrations.AlterField(
            model_name='airflow',
            name='leedVot',
            field=models.DecimalField(decimal_places=2, max_digits=11),
        ),
        migrations.AlterField(
            model_name='airflow',
            name='occupants',
            field=models.DecimalField(decimal_places=2, max_digits=11),
        ),
        migrations.AlterField(
            model_name='airflow',
            name='occupiedIdleAirflow',
            field=models.DecimalField(decimal_places=2, max_digits=11),
        ),
        migrations.AlterField(
            model_name='airflow',
            name='occupiedMaxAirflow',
            field=models.DecimalField(decimal_places=2, max_digits=11),
        ),
        migrations.AlterField(
            model_name='airflow',
            name='occupiedReqAirflow',
            field=models.DecimalField(decimal_places=2, max_digits=11),
        ),
        migrations.AlterField(
            model_name='airflow',
            name='raOutAirRateArea',
            field=models.DecimalField(decimal_places=2, max_digits=11),
        ),
        migrations.AlterField(
            model_name='airflow',
            name='raOutAirRatePerson',
            field=models.DecimalField(decimal_places=2, max_digits=11),
        ),
        migrations.AlterField(
            model_name='airflow',
            name='reqDamperPosition',
            field=models.DecimalField(decimal_places=2, max_digits=11),
        ),
        migrations.AlterField(
            model_name='airflow',
            name='vbz',
            field=models.DecimalField(decimal_places=2, max_digits=11),
        ),
        migrations.AlterField(
            model_name='airflow',
            name='vot',
            field=models.DecimalField(decimal_places=2, max_digits=11),
        ),
        migrations.AlterField(
            model_name='airflow',
            name='voz',
            field=models.DecimalField(decimal_places=2, max_digits=11),
        ),
    ]
