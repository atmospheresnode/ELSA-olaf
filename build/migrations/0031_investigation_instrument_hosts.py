# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2022-11-17 17:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('build', '0030_remove_investigation_instrument_hosts'),
    ]

    operations = [
        migrations.AddField(
            model_name='investigation',
            name='instrument_hosts',
            field=models.ManyToManyField(to='build.Instrument_Host'),
        ),
    ]
