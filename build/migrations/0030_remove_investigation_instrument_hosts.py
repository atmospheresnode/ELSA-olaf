# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2022-11-17 17:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('build', '0029_auto_20221116_1420'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='investigation',
            name='instrument_hosts',
        ),
    ]