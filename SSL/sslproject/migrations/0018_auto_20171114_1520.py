# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-14 15:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sslproject', '0017_education'),
    ]

    operations = [
        migrations.RenameField(
            model_name='education',
            old_name='institue',
            new_name='institute',
        ),
    ]
