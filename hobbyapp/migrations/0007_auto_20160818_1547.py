# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-18 15:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hobbyapp', '0006_auto_20160818_1547'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ('email',)},
        ),
    ]
