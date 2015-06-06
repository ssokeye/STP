# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0009_auto_20150606_0534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='members',
            name='Family_Class',
            field=models.CharField(blank=True, max_length=10, choices=[(b'P', b'Parent'), (b'C', b'Child')]),
        ),
        migrations.AlterField(
            model_name='members',
            name='Married_Status',
            field=models.CharField(blank=True, max_length=10, choices=[(b'Married', b'Married'), (b'Single', b'Single')]),
        ),
    ]
