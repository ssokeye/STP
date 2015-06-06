# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0008_auto_20150424_0337'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member_Training',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Date_Completed', models.DateField(default=datetime.date.today)),
            ],
        ),
        migrations.CreateModel(
            name='Training',
            fields=[
                ('Training_Id', models.AutoField(serialize=False, primary_key=True)),
                ('Training_Name', models.CharField(max_length=100)),
                ('Created_By', models.CharField(max_length=30)),
                ('Date_Created', models.DateTimeField(default=datetime.datetime.now)),
                ('Modified_By', models.CharField(max_length=30)),
                ('last_Modified', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.RenameField(
            model_name='departments',
            old_name='Dept_ID',
            new_name='Dept_Id',
        ),
        migrations.RenameField(
            model_name='member_department',
            old_name='Dept_id',
            new_name='Dept_Id',
        ),
        migrations.RenameField(
            model_name='member_department',
            old_name='Member_id',
            new_name='Member_Id',
        ),
        migrations.AddField(
            model_name='members',
            name='Family_Class',
            field=models.CharField(default=b'none', max_length=10, choices=[(b'P', b'Parent'), (b'C', b'Child')]),
        ),
        migrations.AddField(
            model_name='members',
            name='Married_Status',
            field=models.CharField(default=b'none', max_length=10, choices=[(b'Married', b'Married'), (b'Single', b'Single')]),
        ),
        migrations.AlterField(
            model_name='members',
            name='Gender',
            field=models.CharField(blank=True, max_length=10, choices=[(b'M', b'Male'), (b'F', b'Female')]),
        ),
        migrations.AddField(
            model_name='member_training',
            name='Member_Id',
            field=models.ForeignKey(to='members.Members'),
        ),
        migrations.AddField(
            model_name='member_training',
            name='Training_Id',
            field=models.ForeignKey(to='members.Training'),
        ),
    ]
