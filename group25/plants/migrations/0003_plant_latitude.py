# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-03 05:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0002_plant_actuator_value'),
    ]

    operations = [
        migrations.AddField(
            model_name='plant',
            name='latitude',
            field=models.CharField(default=13.5572, max_length=250),
            preserve_default=False,
        ),
    ]
