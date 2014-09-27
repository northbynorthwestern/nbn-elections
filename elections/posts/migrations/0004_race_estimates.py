# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20140924_1435'),
    ]

    operations = [
        migrations.AddField(
            model_name='race',
            name='estimates',
            field=jsonfield.fields.JSONField(null=True),
            preserve_default=True,
        ),
    ]
