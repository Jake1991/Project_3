# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0021_auto_20160412_1905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='simplequestion',
            name='image',
            field=models.ImageField(upload_to='static/question_images', blank=True),
        ),
    ]
