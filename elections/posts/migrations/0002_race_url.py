# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='race',
            name='url',
            field=models.URLField(max_length=250, unique=True, null=True),
            preserve_default=True,
        ),
    ]
