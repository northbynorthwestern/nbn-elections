# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20140918_2028'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.ManyToManyField(to='posts.Author', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='post',
            name='posted_datetime',
            field=models.DateTimeField(db_index=True, auto_now_add=True, null=True),
            preserve_default=True,
        ),
    ]
