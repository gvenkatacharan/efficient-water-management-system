# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-21 16:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0005_auto_20171121_1548'),
    ]

    operations = [
        migrations.RenameField(
            model_name='plantcondition',
            old_name='plant',
            new_name='plant_id',
        ),
    ]
