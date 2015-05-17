# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_auto_20150424_0157'),
    ]

    operations = [
        migrations.AddField(
            model_name='departments',
            name='Date_Created',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='departments',
            name='last_Modified',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='member_department',
            name='Date_Created',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='member_department',
            name='last_Modified',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='members',
            name='Birth_Date',
            field=models.DateField(default=datetime.date.today, verbose_name=b'Date of Birth'),
        ),
        migrations.AddField(
            model_name='members',
            name='Date_Created',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='members',
            name='Date_Joined',
            field=models.DateField(default=datetime.date.today, verbose_name=b'Date Joined'),
        ),
        migrations.AddField(
            model_name='members',
            name='last_Modified',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
