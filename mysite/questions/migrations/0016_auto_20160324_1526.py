# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0015_auto_20160214_1519'),
    ]

    operations = [
        migrations.AddField(
            model_name='simplequestion',
            name='exam_board',
            field=models.CharField(max_length=100, default=''),
        ),
        migrations.AlterField(
            model_name='dayscore',
            name='date',
            field=models.DateField(default=datetime.date(2016, 3, 24)),
        ),
    ]
