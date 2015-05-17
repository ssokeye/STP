# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0006_auto_20150424_0257'),
    ]

    operations = [
        migrations.AddField(
            model_name='members',
            name='Gender',
            field=models.CharField(default=b'none', max_length=10, choices=[(b'M', b'Male'), (b'F', b'Female'), (b'none', b'None')]),
        ),
    ]
