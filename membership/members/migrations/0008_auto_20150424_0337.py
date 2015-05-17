# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0007_members_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='members',
            name='Gender',
            field=models.CharField(max_length=10, choices=[(b'M', b'Male'), (b'F', b'Female')]),
        ),
    ]
