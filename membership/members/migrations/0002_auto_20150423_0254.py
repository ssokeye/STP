# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member_department',
            old_name='Dept',
            new_name='Dept_id',
        ),
        migrations.RenameField(
            model_name='member_department',
            old_name='Member',
            new_name='Member_id',
        ),
    ]
