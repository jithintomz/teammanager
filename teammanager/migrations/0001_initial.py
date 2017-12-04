# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-12-04 09:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=30, null=True)),
                ('last_name', models.CharField(blank=True, max_length=30, null=True)),
                ('phoneno', models.CharField(blank=True, max_length=40, null=True)),
                ('email', models.CharField(blank=True, max_length=200, null=True)),
                ('role', models.IntegerField(default=1)),
            ],
        ),
    ]
