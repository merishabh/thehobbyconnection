# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-23 11:32
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('access_token', models.CharField(max_length=150)),
                ('facebook_id', models.BigIntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HobbyGroup',
            fields=[
                ('hobby_id', models.AutoField(primary_key=True, serialize=False)),
                ('hobby_name', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='HobbyGroupUser',
            fields=[
                ('hobby_group_id', models.AutoField(primary_key=True, serialize=False)),
                ('hobby', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hobbyapp.HobbyGroup')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
