# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0017_simplequestion_standalone'),
    ]

    operations = [
        migrations.AddField(
            model_name='simplequestion',
            name='module',
            field=models.CharField(max_length=100, default=''),
        ),
    ]
