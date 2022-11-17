# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2022-11-04 14:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('build', '0011_auto_20221104_0730'),
    ]

    operations = [
        migrations.AddField(
            model_name='investigation',
            name='instrument_hosts',
            field=models.ManyToManyField(to='build.Instrument_Host'),
        ),
        migrations.AddField(
            model_name='investigation',
            name='targets',
            field=models.ManyToManyField(to='build.Target'),
        ),
    ]
