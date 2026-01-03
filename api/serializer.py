from rest_framework import serializers
from DBAPP.models import Employee,Department

class EmpSerializer(serializers.ModelSerializer):
      class Meta:
            model = Employee
            fields = ['Employee_No',"Employee_Name","Employee_Salary","department"]

