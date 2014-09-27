# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_race_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='race',
            name='last_updated',
            field=models.DateTimeField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='race',
            name='poll_count',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
    ]
