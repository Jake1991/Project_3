# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-14 15:19
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0014_auto_20160213_1643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dayscore',
            name='date',
            field=models.DateField(default=datetime.date(2016, 2, 14)),
        ),
    ]