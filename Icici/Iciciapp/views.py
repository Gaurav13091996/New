from django.shortcuts import render,HttpResponseRedirect,redirect
from django.shortcuts import render
from .models import Employee_Details
from rest_framework.views import APIView
from rest_framework.viewsets import views
from .serializer import Employeeserializer
from rest_framework.response import Response
from .form import EmployeeRegistration
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required


# Create your views here.

def show(r):
    results=Employee_Details.objects.all().order_by('id')
    print(results)
    return render(r,'display.html',{'data':results})

class Employee_list(APIView):
    def get(self,request):
        Employees = Employee_Details.objects.all()
        employee_serializer = Employeeserializer(Employees, many=True)
        return Response(employee_serializer.data)

@login_required()
def Employee_Regi(request):
    if request.method == 'POST':
        fm = EmployeeRegistration(request.POST)
        print(fm)
        if fm.is_valid():
            id=fm.cleaned_data['id']
            name=fm.cleaned_data['name']
            age=fm.cleaned_data['age']
            designation=fm.cleaned_data['designation']
            doj=fm.cleaned_data['doj']
            print(id)
            print(name)
            print(age)
            fm.save()
            return redirect('/')

    else:
            fm = EmployeeRegistration()
    return render(request,'registration.html',{'form':fm})
    return HttpResponseRedirect('/')
@login_required()
def update(request,id):
    if request.method=='POST':
        updatedata=Employee_Details.objects.get(id=id)
        form=EmployeeRegistration(request.POST,instance=updatedata)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        updatedata = Employee_Details.objects.get(id=id)
        form = EmployeeRegistration(instance=updatedata)
    return render(request,'update.html',{'form':form})

def deletedata(request,id):
    if request.method=='POST':
        pi=Employee_Details.objects.get(pk=id)
        print(pi)
        pi.delete()
    return HttpResponseRedirect('/')

def signup(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        user=User.objects.create_user(username=username,password=password1,email=email)
        user.save()
        print('user created')
        return redirect('/')
    return render(request,'signup.html')


 