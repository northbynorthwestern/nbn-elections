# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20140918_2028'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='status',
            field=models.CharField(default=b'd', max_length=1, null=True, choices=[(b'd', b'Draft'), (b'r', b'Read Me'), (b'e', b'Edited'), (b'p', b'Published')]),
            preserve_default=True,
        ),
    ]
