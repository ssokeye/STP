# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_auto_20150423_0254'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='departments',
            name='last_Modified',
        ),
        migrations.RemoveField(
            model_name='member_department',
            name='last_Modified',
        ),
        migrations.RemoveField(
            model_name='members',
            name='last_Modified',
        ),
    ]
