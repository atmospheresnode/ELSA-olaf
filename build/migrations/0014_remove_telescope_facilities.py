# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2023-03-30 05:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('build', '0013_auto_20230324_1415'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='telescope',
            name='facilities',
        ),
    ]