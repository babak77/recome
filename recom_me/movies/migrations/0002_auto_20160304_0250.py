# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-04 01:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gener',
            name='desc',
        ),
        migrations.RemoveField(
            model_name='gener',
            name='timestamp',
        ),
        migrations.RemoveField(
            model_name='gener',
            name='update',
        ),
    ]