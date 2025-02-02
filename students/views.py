from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import models

# Create your views here.

def home(request):
    return render(request, 'home.html')

def addStudent(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        photo = request.FILES.get('photo')
    

        student= models.Students(name=name, email=email, address=address, phone=phone, password=password, photo=photo)
        student.save()
        return redirect("home")
        
    return render(request, 'addstudent.html')


def allStudents(request):
    students = models.Students.objects.all()
    return render(request,'allstudents.html', {'students': students})


def update_students(request, id):
    student = models.Students.objects.get(id=id)

    if request.method == 'POST':
        student.name = request.POST.get('name')
        student.email = request.POST.get('email')
        student.address = request.POST.get('address')
        student.phone = request.POST.get('phone')
        student.password = request.POST.get('password')
        student.photo = request.FILES.get('photo')
    
        student.save()
        return redirect("allStudents")  # Adjust according to your URL names

    return render(request, 'update_student.html', {'student': student})


def delete_students(request, id):
    student = models.Students.objects.get(id=id)
    student.delete()
    return redirect ("allStudents")  # Adjust according to your URL names