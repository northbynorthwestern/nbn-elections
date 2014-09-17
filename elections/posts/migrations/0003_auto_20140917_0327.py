# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20140914_1950'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='posted_date',
        ),
        migrations.AddField(
            model_name='post',
            name='posted_datetime',
            field=models.DateTimeField(default=datetime.datetime.now, auto_now_add=True, db_index=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='post',
            name='status',
            field=models.CharField(default=datetime.datetime(2014, 9, 17, 3, 27, 29, 629505), max_length=1, choices=[(b'd', b'Draft'), (b'p', b'Read Me'), (b'p', b'Edited'), (b'p', b'Published')]),
            preserve_default=False,
        ),
    ]
