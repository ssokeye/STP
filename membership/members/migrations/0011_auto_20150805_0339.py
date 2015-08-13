# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0010_auto_20150606_0548'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('Dept_Id', models.AutoField(serialize=False, primary_key=True)),
                ('Dept_Name', models.CharField(max_length=100)),
                ('Dept_HOD', models.CharField(max_length=100)),
                ('Created_By', models.CharField(max_length=30)),
                ('Date_Created', models.DateTimeField(default=datetime.datetime.now)),
                ('Modified_By', models.CharField(max_length=30)),
                ('last_Modified', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('Member_Id', models.AutoField(serialize=False, primary_key=True)),
                ('First_Name', models.CharField(max_length=30)),
                ('Middle_Name', models.CharField(max_length=30)),
                ('Last_Name', models.CharField(max_length=30)),
                ('Birth_Date', models.DateField(default=datetime.date.today, verbose_name=b'Date of Birth')),
                ('Gender', models.CharField(blank=True, max_length=10, choices=[(b'M', b'Male'), (b'F', b'Female')])),
                ('Address1', models.CharField(max_length=100)),
                ('Address2', models.CharField(max_length=100)),
                ('City', models.CharField(max_length=30)),
                ('State', models.CharField(max_length=30)),
                ('Zip', models.CharField(max_length=10)),
                ('Home_Phone', models.CharField(max_length=30)),
                ('Cell_Phone', models.CharField(max_length=30)),
                ('Work_Phone', models.CharField(max_length=30)),
                ('Email_Address', models.EmailField(max_length=100)),
                ('Date_Joined', models.DateField(default=datetime.date.today, verbose_name=b'Date Joined')),
                ('Married_Status', models.CharField(blank=True, max_length=10, choices=[(b'Married', b'Married'), (b'Single', b'Single')])),
                ('Member_Class', models.CharField(max_length=30)),
                ('Family_Class', models.CharField(blank=True, max_length=10, choices=[(b'P', b'Parent'), (b'C', b'Child')])),
                ('Created_By', models.CharField(max_length=30)),
                ('Date_Created', models.DateTimeField(default=datetime.datetime.now)),
                ('Modified_By', models.CharField(max_length=30)),
                ('last_Modified', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.AlterField(
            model_name='member_department',
            name='Dept_Id',
            field=models.ForeignKey(to='members.Department'),
        ),
        migrations.AlterField(
            model_name='member_department',
            name='Member_Id',
            field=models.ForeignKey(to='members.Member'),
        ),
        migrations.AlterField(
            model_name='member_training',
            name='Member_Id',
            field=models.ForeignKey(to='members.Member'),
        ),
        migrations.DeleteModel(
            name='Departments',
        ),
        migrations.DeleteModel(
            name='Members',
        ),
    ]
