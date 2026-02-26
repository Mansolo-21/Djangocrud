from django.shortcuts import render
from .models import Student
from . forms import StudentForm
# Create your views here.
def index (request):
    return render(request,'myapp/index.html')

#crud
#c-create-add a record into db
def create_student(request):
     if request.method == 'POST':
        firstname = request.POST.get('name')
        lastname = request.POST.get('email')
        age = request.POST.get('subject')
        course= request.POST.get('message')

        # Save to database
        StudentForm.objects.create(
            firstname=firstname,
            lastname=lastname,
            age=age,
            course=course
        )
        form=StudentForm()
        return render(request,'myapp/studentform.html',{'form':form})
    
def admin(request):
    return render(request,'myapp/admindashboard.html')



