from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,'crud_app/home.html')

def form(request):
    if request.method =='POST' or request.FILES:
        name = request.POST['name']
        age = request.POST['age']
        email = request.POST['email']
        message = request.POST['message']
        dob = request.POST['dob']
        image = request.FILES.get('image')
        
        Students.objects.create(name=name,age=age,email=email,message=message,dob=dob,image=image)
       
        messages.success(request,f"hi {name} your message is submitted")
        return redirect('form')
      
    return render(request,'crud_app/form.html')

# show result of form
def show(request):
    data = Students.objects.all()
    return render(request,'crud_app/result.html',{'data':data})

def about(request):
    return render(request,'crud_app/about.html')

def contact(request):
    return render(request,'crud_app/contact.html')