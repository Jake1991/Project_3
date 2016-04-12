# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0018_simplequestion_module'),
    ]

    operations = [
        migrations.AddField(
            model_name='simplequestion',
            name='image',
            field=models.ImageField(blank=True, upload_to='question_images'),
        ),
        migrations.AlterField(
            model_name='dayscore',
            name='date',
            field=models.DateField(default=datetime.date(2016, 4, 12)),
        ),
    ]
