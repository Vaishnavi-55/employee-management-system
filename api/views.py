from rest_framework.views import APIView
from DBAPP.models import Employee,Department
from .serializer import EmpSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
# Create your views here.

#ModelViewSet for CRUD Operations
# class EmployeeViewSet(ModelViewSet):
#     queryset = Employee.objects.all()
#     serializer_class = EmpSerializer

#Normal ClassBasedView for CRUD Operations
class EmployeeCreateView(APIView):
      def get(self,request):
          emp_obj = Employee.objects.all()
          serializer = EmpSerializer(emp_obj,many=True)
          return Response(serializer.data)
      def post(self,request):
          serializer_obj = EmpSerializer(data=request.data)
          if serializer_obj.is_valid():
             serializer_obj.save()
             return Response({"message":"Employee Created Successfully"},status=status.HTTP_201_CREATED)
          return Response(serializer_obj.errors,status=status.HTTP_400_BAD_REQUEST)
      
class EmployeeModifyView(APIView):
      def get(self,request,pk):
          try:
            emp = Employee.objects.get(Employee_No=pk)
            serializer_obj = EmpSerializer(emp)
            return Response(serializer_obj.data,status=status.HTTP_200_OK)
          except Employee.DoesNotExist:
              return Response({"error":"Employee No Found"},status=status.HTTP_404_NOT_FOUND)
          
      def put(self,request,pk):
          try:
            emp = Employee.objects.get(Employee_No=pk)
          except Employee.DoesNotExist:
              return Response({"error":"Employee No Found"},status=status.HTTP_404_NOT_FOUND)
          serializer_obj = EmpSerializer(emp,data=request.data)
          if serializer_obj.is_valid():
             serializer_obj.save()
             return Response(serializer_obj.data,status=status.HTTP_200_OK)
          return Response(serializer_obj.errors,status=status.HTTP_400_BAD_REQUEST)
      def Patch(self,request,pk):
          try:
              emp = Employee.objects.get(Employee_No=pk)
          except Employee.DoesNotExist:
              return Response({"error":"Employee No Found"},status=status.HTTP_404_NOT_FOUND)
          serializer_obj = EmpSerializer(emp,data=request.data)
          if serializer_obj.is_valid():
             serializer_obj.save()
             return Response(serializer_obj.data,status=status.HTTP_200_OK)
          return Response(serializer_obj.errors,status=status.HTTP_400_BAD_REQUEST)
      def delete(self,request,pk):
          try:
              emp = Employee.objects.get(Employee_No=pk)
          except Employee.DoesNotExist:
              return Response({"error":"Employee No Found"},status=status.HTTP_404_NOT_FOUND)
          emp.delete()
          return Response({"message":"Employee deleted"},status=status.HTTP_204_NO_CONTENT)
          

          