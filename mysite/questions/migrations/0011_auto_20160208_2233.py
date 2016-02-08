# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0010_auto_20160206_1923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dayscore',
            name='date',
            field=models.DateField(default=datetime.date(2016, 2, 8)),
        ),
    ]
