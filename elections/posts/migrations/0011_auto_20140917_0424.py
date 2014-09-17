# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0010_post_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='posted_datetime',
        ),
        migrations.RemoveField(
            model_name='post',
            name='status',
        ),
    ]
