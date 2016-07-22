# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-21 09:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='gender',
            field=models.CharField(default='male', max_length=10),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='info',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='phone',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='score',
            field=models.FloatField(default=0),
        ),
    ]
