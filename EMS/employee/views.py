from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import employees
from .utils import checkRegistration

# Create your views here.

def home(request):
    return HttpResponse(render(request,"home.html"))

def addemployee(request):
    emp= employees()
    if request.method== "POST":
        name= request.POST.get("name")
        contact= request.POST.get("contact")
        email= request.POST.get("email")
        department= request.POST.get("department")
        salary= request.POST.get("salary")
        password= request.POST.get("password")
        
        isAlreadyregistred= checkRegistration(email)

        if isAlreadyregistred:
            return HttpResponse(render(request,"addemp.html",{'message':"email is already registred"}))
        
        else:
            emp.name= name
            emp.contact= contact
            emp.email= email
            emp.department= department
            emp.salary= salary
            emp.password= password
            emp.save()
            return HttpResponse(render(request,"addemp.html",{'message':"registred successful"}))
        

    else:
        return HttpResponse(render(request,"addemp.html",{}))








def viewemployee(request):
    data= employees.objects.all()
    return HttpResponse(render(request,"showemp.html",{'empdata':data}))



def deleteemployee(request, emp_id):
    data= employees.objects.get(id=emp_id)
    

    if request.method== "POST":
        password= request.POST.get("password")
        
        if data.password== password:
            data.delete()
            return redirect('/employee/')

        else:
            return HttpResponse(render(request,"delemp.html",{'emp_data':data, 'message':"wrong password"}))

    else:
        return HttpResponse(render(request,"delemp.html",{'emp_data':data}))



def updateemployee(request, emp_id):
    data= employees.objects.get(id=emp_id)
    return HttpResponse(render(request,"update-emp.html",{'emp_data':data}))

def doUpdate(request, emp_id):
    emp= employees.objects.get(id=emp_id)
    if request.method== "POST":
        name= request.POST.get("name")
        contact= request.POST.get("contact")
        email= request.POST.get("email")
        department= request.POST.get("department")
        salary= request.POST.get("salary")

        emp.name= name
        emp.contact= contact
        emp.email= email
        emp.department= department
        emp.salary= salary
        emp.save()
        return redirect('/employee/')

    else:
        return HttpResponse(render(request,"update-emp.html",{'emp_data':emp}))



        