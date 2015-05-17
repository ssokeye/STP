# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departments',
            fields=[
                ('Dept_ID', models.AutoField(serialize=False, primary_key=True)),
                ('Dept_Name', models.CharField(max_length=100)),
                ('Dept_HOD', models.CharField(max_length=100)),
                ('Created_By', models.CharField(max_length=30)),
                ('Modified_By', models.CharField(max_length=30)),
                ('last_Modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Member_Department',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Status', models.CharField(max_length=10)),
                ('Created_By', models.CharField(max_length=30)),
                ('Modified_By', models.CharField(max_length=30)),
                ('last_Modified', models.DateTimeField(auto_now=True)),
                ('Dept', models.ForeignKey(to='members.Departments')),
            ],
        ),
        migrations.CreateModel(
            name='Members',
            fields=[
                ('Member_Id', models.AutoField(serialize=False, primary_key=True)),
                ('First_Name', models.CharField(max_length=30)),
                ('Middle_Name', models.CharField(max_length=30)),
                ('Last_Name', models.CharField(max_length=30)),
                ('Address1', models.CharField(max_length=100)),
                ('Address2', models.CharField(max_length=100)),
                ('City', models.CharField(max_length=30)),
                ('State', models.CharField(max_length=30)),
                ('Zip', models.CharField(max_length=10)),
                ('Home_Phone', models.CharField(max_length=30)),
                ('Cell_Phone', models.CharField(max_length=30)),
                ('Work_Phone', models.CharField(max_length=30)),
                ('Email_Address', models.EmailField(max_length=100)),
                ('Member_Class', models.CharField(max_length=30)),
                ('Created_By', models.CharField(max_length=30)),
                ('Modified_By', models.CharField(max_length=30)),
                ('last_Modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='member_department',
            name='Member',
            field=models.ForeignKey(to='members.Members'),
        ),
    ]
