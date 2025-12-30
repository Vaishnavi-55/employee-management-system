from django.shortcuts import render,redirect
from django.http import HttpResponse
from DBAPP.models import Employee,Department
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
# Create your views here.
def signup(request):
    if request.method == 'POST':
       email = request.POST['mail']
       username = request.POST['usname']
       password = request.POST['paswrd1']
       confirm_password = request.POST['paswrd2']
       if password != confirm_password:
          return render(request,'EmployeeApp/signup.html',{'error':'passwords do not match'})
       elif User.objects.filter(username=username).exists():
            return render(request,'EmployeeApp/signup.html',{'error':'This username already exists'})
       else:
          User.objects.create_user(username=username,password=password,email=email)
          return redirect('super:login.url')
    return render(request,'EmployeeApp/signup.html')

def Login(request):
    if request.method == 'GET':
        return render(request,'EmployeeApp/Login.html')
    if request.method == 'POST':
       username = request.POST['usname']
       password = request.POST['paswrd']
       user = authenticate(request,username=username,password=password)
       if user is not None:
          login(request,user)
          if user.is_superuser:
             return render(request,'EmployeeApp/super.html')
          else:
             return redirect('DBAPP:showdetails.url')
       else:
           return render(request,'EmployeeApp/Login.html',{'error':'Invalid Username or Password'})
    return render(request,'EmployeeApp/Login.html')

def Logout(request):
   logout(request)
   return redirect('super:login.url')

