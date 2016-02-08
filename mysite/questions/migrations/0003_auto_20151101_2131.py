# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0002_usersession'),
    ]

    operations = [
        migrations.AddField(
            model_name='usersession',
            name='last_updated',
            field=models.DateField(default=datetime.date(2015, 1, 1)),
        ),
        migrations.AlterField(
            model_name='usersession',
            name='score',
            field=models.IntegerField(default=0),
        ),
    ]
