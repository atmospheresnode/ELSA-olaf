# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2022-11-03 17:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('build', '0004_auto_20221021_1450'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sandwich',
            name='meats',
        ),
        migrations.RemoveField(
            model_name='sandwich',
            name='veggies',
        ),
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
        migrations.DeleteModel(
            name='Meat',
        ),
        migrations.DeleteModel(
            name='Sandwich',
        ),
        migrations.DeleteModel(
            name='Veggie',
        ),
    ]
