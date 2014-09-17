# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_auto_20140917_0401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(default=b'd', max_length=1, choices=[(b'd', b'Draft'), (b'p', b'Read Me'), (b'p', b'Edited'), (b'p', b'Published')]),
        ),
    ]
