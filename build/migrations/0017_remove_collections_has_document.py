# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2022-11-04 20:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('build', '0016_investigation_instrument_hosts'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='collections',
            name='has_document',
        ),
    ]