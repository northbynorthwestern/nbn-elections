# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_auto_20141003_0424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='posted_datetime',
            field=models.DateTimeField(null=True, db_index=True),
        ),
    ]
