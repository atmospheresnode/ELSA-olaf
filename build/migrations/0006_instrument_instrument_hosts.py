# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2022-11-03 17:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('build', '0005_auto_20221103_1004'),
    ]

    operations = [
        migrations.AddField(
            model_name='instrument',
            name='instrument_hosts',
            field=models.ManyToManyField(to='build.Instrument_Host'),
        ),
    ]
