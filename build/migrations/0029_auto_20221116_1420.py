# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2022-11-16 21:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('build', '0028_auto_20221116_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facility',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='instrument_host',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='target',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='telescope',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
