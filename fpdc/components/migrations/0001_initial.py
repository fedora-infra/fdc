# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-02-01 13:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RPMPackage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('point_of_contact', models.CharField(max_length=100)),
            ],
        ),
    ]
