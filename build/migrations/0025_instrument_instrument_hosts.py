# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2022-11-15 18:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('build', '0024_remove_instrument_instrument_hosts'),
    ]

    operations = [
        migrations.AddField(
            model_name='instrument',
            name='instrument_hosts',
            field=models.ManyToManyField(to='build.Instrument_Host'),
        ),
    ]
