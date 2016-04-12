# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0019_auto_20160412_1844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='simplequestion',
            name='image',
            field=models.ImageField(blank=True, upload_to='/questions/static/question_images'),
        ),
    ]
