from django.shortcuts import render,redirect,get_object_or_404
from .models import Student
from . forms import StudentForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from . forms import RegisterForm
from django.contrib.auth import login,logout
# Create your views here.
def index (request):
    return render(request,'User/index.html')

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

    return render(request, 'Admin/studentform.html', {'form': form})
#c-create-add a record into db

 

def read_students(request):
    students=Student.objects.all()
    return render(request, 'Admin/admindashboard.html',{'students':students})

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

    return render(request, 'Admin/studentform.html', {'form': form})

def register_user(request):

    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            print("✅ USER SAVED")   # DEBUG
            return redirect('students')
        else:
            print(form.errors)       # ⭐ VERY IMPORTANT

    else:
        form = RegisterForm()

    return render(request, 'User/register.html', {'form': form})

def login_user(request):

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)

            # redirect depending on user type
            if user.is_staff:
                return redirect('students')   # admin dashboard
            else:
                return redirect('user')       # user dashboard
    else:
        form = AuthenticationForm()

    return render(request, 'User/login.html', {'form': form})
            
def user_dashboard(request):
    return render(request, 'User/userdashboard.html')

def logout_user(request):
    logout(request)
    return redirect('login')

