# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_auto_20140917_0356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='posted_datetime',
            field=models.DateTimeField(auto_now_add=True, db_index=True),
        ),
    ]
