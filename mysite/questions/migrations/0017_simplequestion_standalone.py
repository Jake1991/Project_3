# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0016_auto_20160324_1526'),
    ]

    operations = [
        migrations.AddField(
            model_name='simplequestion',
            name='standalone',
            field=models.BooleanField(default=True),
        ),
    ]
