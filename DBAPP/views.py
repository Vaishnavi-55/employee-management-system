from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Employee,Department
from django.contrib.auth.decorators import login_required,user_passes_test
from django.core.paginator import Paginator

# Create your views here.
def is_superuser(user):
    return user.is_superuser
@login_required(login_url='super:login.url')
@user_passes_test(is_superuser,login_url='super:login.url')
def insert(request):
    departments = Department.objects.all()
    if request.method == 'GET':
       return render(request,'employee/insert.html',{'departments':departments})
    if request.method == 'POST':
       if 'show' in request.POST:
          return redirect('showdetails.url')
       empno = int(request.POST['empno'])
       empname = request.POST['empname']
       esal = int(request.POST['esal'])
       dept_name = request.POST['dept']
       img = request.FILES.get('image')
       res = result = ''
       try:
         dept,created = Department.objects.get_or_create(Department_Name = dept_name)
         eobj = Employee.objects.create(Employee_No=empno,Employee_Name=empname,Employee_Salary=esal,department=dept,Images=img)
       except Exception:
         res ='You Dont have an access To insert'
       else:
          result = f'Inserted Successfully {empno} details'
       return render(request,'employee/insert.html',{'res':res,'ress':result})
    
@login_required(login_url='super:login.url')
def show(request):
      res = Employee.objects.all()
      Paginate = Paginator(res,2)
      page_number = request.GET.get('page')
      page_obj = Paginate.get_page(page_number)
      return render(request,'employee/showdetails.html',{'page_obj':page_obj})

@login_required(login_url='super:login.url')
@user_passes_test(is_superuser,login_url='super:login.url')
def update(request,eno):
   emp = Employee.objects.get(Employee_No = eno)
   depts = Department.objects.all()
   if request.method == 'GET':
      return render(request,'employee/update.html',{'employee':emp,'department':depts})
   if request.method == 'POST':
       try:
         empname = request.POST['empname']
         esal = int(request.POST['esal'])
         dept_name = request.POST['dept']
         emp.Employee_Name = empname
         emp.Employee_Salary = esal
         emp.department_id = dept_name
         emp.save()
       except Exception:
         result ='You Dont have an access To Update'
       else:
        result = f'Updated Successfully {eno} details'
       return render(request,'employee/update.html',{'ress':result})
      
@login_required(login_url='super:login.url')
@user_passes_test(is_superuser,login_url='super:login.url')
def delete(request,eno):
   if request.method == 'GET':
      try:
         obj = Employee.objects.get(Employee_No=eno)
      except:
         return render(request,'employee/delete.html',{'error':'There is no such user'})
      return render(request,'employee/delete.html',{'obj':obj})

   if request.method == 'POST':
        try:
          obj = Employee.objects.get(Employee_No=eno)
          obj.delete()
        except:
          return render(request,'employee/delete.html',{'error':'You dont have an access to delete'})
        else:
           return  render(request,'employee/delete.html',{'error':'Deleted successfully'})

@login_required(login_url='super:login.url')
@user_passes_test(is_superuser,login_url='super:login.url')       
def details(request):
    if request.user.is_superuser:
      if request.method == 'GET':
         print(request.GET)
         return render(request,'EmployeeApp/super.html')
      elif request.method == 'POST':
           print(request.POST)
           empno = int(request.POST['empno'])
         #   enpo = int(request.POST['eno'])
           obju = Employee.objects.get(Employee_No=empno)
         #   objd = Employee.objects.get(Employee_No=enpo)
           print(obju.Employee_No)
           return render(request,'EmployeeApp/super.html',{'obju':obju})
      else:
         return redirect('super:login.url')
