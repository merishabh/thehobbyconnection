# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-19 06:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hobbyapp', '0008_auto_20160818_1548'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.CharField(blank=True, default='', max_length=1000, verbose_name='image'),
        ),
    ]
