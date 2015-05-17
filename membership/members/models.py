from django.db import models
from datetime import date, datetime

# Create your models here.

#Church Members
class Members(models.Model):
	Member_Id = models.AutoField(primary_key=True)
	Family_Id = models.IntegerField #(primary_key=False)
	First_Name = models.CharField(max_length=30)
	Middle_Name = models.CharField(max_length=30)
	Last_Name = models.CharField(max_length=30)
	Birth_Date = models.DateField('Date of Birth',default=date.today)
	Gender = models.CharField(max_length=10, choices=(('M','Male'),('F','Female'),))
	Address1 = models.CharField(max_length=100)
	Address2 = models.CharField(max_length=100)
	City = models.CharField(max_length=30)
	State = models.CharField(max_length=30)
	Zip = models.CharField(max_length=10)
	Home_Phone = models.CharField(max_length = 30)
	Cell_Phone = models.CharField(max_length = 30)
	Work_Phone = models.CharField(max_length = 30)
	Email_Address = models.EmailField(max_length=100)
	Date_Joined = models.DateField('Date Joined',default=date.today)
	Worker_Ind = models.BooleanField
	Married_Status = models.CharField(max_length=10, choices=(('Married','Married'),('Single','Single'),))
	Is_Member_Status = models.BooleanField
	Member_Class = models.CharField(max_length=30)
	Family_Class = models.CharField(max_length=10, choices=(('P','Parent'),('C','Child'),)) #(Create as Tupel Parent/Children)
	Created_By = models.CharField(max_length=30)
	Date_Created = models.DateTimeField(default=datetime.now)
	Modified_By = models.CharField(max_length=30)
	last_Modified = models.DateTimeField(default=datetime.now)

#Church Departments
class Departments(models.Model):
	Dept_Id = models.AutoField(primary_key=True)
	Dept_Name = models.CharField(max_length=100) 
	Dept_HOD = models.CharField(max_length=100) 
	Created_By = models.CharField(max_length=30)
	Date_Created = models.DateTimeField(default=datetime.now)
	Modified_By = models.CharField(max_length=30)
	last_Modified =models.DateTimeField(default=datetime.now)

#Members belonging to a Departments
class Member_Department(models.Model):
	Member_Id = models.ForeignKey('Members')
	Dept_Id = models.ForeignKey('Departments')
	Status = models.CharField(max_length = 10)
	Created_By = models.CharField(max_length=30)
	Date_Created = models.DateTimeField(default=datetime.now)
	Modified_By = models.CharField(max_length=30)
	last_Modified =models.DateTimeField(default=datetime.now)

#Members of Training
class Training(models.Model):
	Training_Id = models.AutoField(primary_key=True)
	Training_Name = models.CharField(max_length = 100)
	Status = models.BooleanField
	Created_By = models.CharField(max_length=30)
	Date_Created = models.DateTimeField(default=datetime.now)
	Modified_By = models.CharField(max_length=30)
	last_Modified = models.DateTimeField(default=datetime.now)

#Members Training
class Member_Training(models.Model):
	Member_Id = models.ForeignKey('Members')
	Training_Id = models.ForeignKey('Training')
	Date_Completed = models.DateField(default=date.today)