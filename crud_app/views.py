from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages


# Create your views here.
def home(request):
    return render(request, "crud_app/home.html")


def form(request):
    if request.method == "POST" or request.FILES:
        name = request.POST["name"]
        age = request.POST["age"]
        email = request.POST["email"]
        message = request.POST["message"]
        dob = request.POST["dob"]
        image = request.FILES.get("image")

        Students.objects.create(
            name=name, age=age, email=email, message=message, dob=dob, image=image
        )

        messages.success(request, f"hi {name} your message is submitted")
        return redirect("form")

    return render(request, "crud_app/form.html")


# show result of form
def show(request):
    data = Students.objects.filter(is_delete = False)
    return render(request, "crud_app/result.html", {"data": data})


def about(request):
    return render(request, "crud_app/about.html")


def contact(request):
    return render(request, "crud_app/contact.html")

def delete_data(request,id):
    data = Students.objects.get(id=id)
    data.is_delete=True
    data.save()
    return redirect('show')

def edit(request,id):
    data = Students.objects.get(id=id)
    if request.method == "POST" or request.FILES:

         data = Students.objects.get(id=id)
         data.name =request.POST["name"]
         data.age =request.POST["age"]
         data.email = request.POST["email"]
         data.message = request.POST["message"]
         dob = request.POST["dob"]
         image =  request.FILES.get("image")
         if image:
             data.image = image
         data.save()
         return redirect('show')
    return render(request,'crud_app/edit.html',{'data':data})

def restoreItem(request):
   data = Students.objects.filter(is_delete=True)
   return render(request,'crud_app/restoreItem.html',{'data':data})

def restore_data(request,id):
    data = Students.objects.get(id=id)
    data.is_delete = False
    data.save()
    return redirect('restore')

def delete_permanent(request,id):
    data = Students.objects.get(id=id)
    data.delete()
    return redirect('restore')
     
def delete_all(request):
    data = Students.objects.filter(is_delete = True)
    # data.update(is_delete=False) 
    data.delete() #permanent delete
    return redirect('restore')
    
