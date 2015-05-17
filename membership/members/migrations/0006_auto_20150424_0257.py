# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0005_auto_20150424_0256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departments',
            name='Date_Created',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='departments',
            name='last_Modified',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='member_department',
            name='Date_Created',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='member_department',
            name='last_Modified',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='members',
            name='Date_Created',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='members',
            name='last_Modified',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
