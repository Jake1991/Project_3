# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-11 18:48
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0011_auto_20160208_2233'),
    ]

    operations = [
        migrations.AddField(
            model_name='multistagequestion',
            name='InterTextFour',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='multistagequestion',
            name='InterTextOne',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='multistagequestion',
            name='InterTextThree',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='multistagequestion',
            name='InterTextTwo',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='dayscore',
            name='date',
            field=models.DateField(default=datetime.date(2016, 2, 11)),
        ),
    ]
