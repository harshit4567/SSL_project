# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-14 08:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sslproject', '0008_employee_designation'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='gender',
            field=models.CharField(default=' ', max_length=100),
        ),
    ]