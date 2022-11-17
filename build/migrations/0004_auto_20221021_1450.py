# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2022-10-21 20:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('build', '0003_auto_20220819_1212'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Sandwich',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('meats', models.ManyToManyField(to='build.Meat')),
            ],
        ),
        migrations.CreateModel(
            name='Veggie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='sandwich',
            name='veggies',
            field=models.ManyToManyField(to='build.Veggie'),
        ),
    ]
