from django.shortcuts import render,redirect,get_object_or_404
from .models import Student
from . forms import StudentForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def index (request):
    return render(request,'myapp/index.html')

#crud
def create_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Student added successfully")
            return redirect('students')
    else:
        form = StudentForm()

    return render(request, 'myapp/studentform.html', {'form': form})
#c-create-add a record into db

 

def read_students(request):
    students=Student.objects.all()
    return render(request, 'myapp/admindashboard.html',{'students':students})

#delete
def delete_student(request,id):
    student=get_object_or_404(Student,pk=id)
    student.delete()
    return redirect('students')

#update
def update_student(request, id):
    student = get_object_or_404(Student, pk=id)

    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request,"Student Data Successfully Updated")
            return redirect('students')
    else:
        form = StudentForm(instance=student)

    return render(request, 'myapp/studentform.html', {'form': form})

def register_user(request):
    form=UserCreationForm()
    if form.is_valid():
        form.save()
    return render(request,'myapp/register.html', {'form': form})
