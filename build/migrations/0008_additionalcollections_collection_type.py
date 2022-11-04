# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2022-11-04 01:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('build', '0007_auto_20221103_1755'),
    ]

    operations = [
        migrations.AddField(
            model_name='additionalcollections',
            name='collection_type',
            field=models.CharField(choices=[('Data', 'Data'), ('Browse', 'Browse'), ('Geometry', 'Geometry'), ('Calibration', 'Calibration'), ('Not_Set', 'Not_Set')], default='Data', max_length=100),
        ),
    ]
