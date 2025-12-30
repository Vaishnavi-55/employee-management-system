from django.db import models

class Department(models.Model):
      Department_No = models.AutoField(primary_key=True)
      Department_Name = models.CharField(max_length=20,unique=True)
class Employee(models.Model):
      Employee_No = models.IntegerField(primary_key=True)
      Employee_Name = models.CharField(max_length=24)
      Employee_Salary = models.IntegerField(null=False)
      department = models.ForeignKey(Department,on_delete=models.CASCADE,null=True,blank=True)
      Images = models.ImageField(null=True,upload_to='image/')

