# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-06-25 19:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='travels',
        ),
        migrations.DeleteModel(
            name='Job',
        ),
    ]