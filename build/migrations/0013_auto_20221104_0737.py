# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2022-11-04 14:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('build', '0012_auto_20221104_0730'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='investigation',
            name='instrument_hosts',
        ),
        migrations.RemoveField(
            model_name='investigation',
            name='targets',
        ),
    ]
