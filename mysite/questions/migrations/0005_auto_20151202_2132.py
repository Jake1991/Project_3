# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0004_auto_20151202_2125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersession',
            name='user_id',
            field=models.IntegerField(default=0),
        ),
    ]
