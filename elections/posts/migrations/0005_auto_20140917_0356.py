# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20140917_0328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='posted_datetime',
            field=models.DateTimeField(default=datetime.datetime(2014, 9, 17, 3, 56, 38, 621301), db_index=True),
        ),
    ]
