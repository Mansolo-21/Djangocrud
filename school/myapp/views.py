from django.shortcuts import render
from . forms import StudentForm
# Create your views here.
def index (request):
    return render(request,'myapp/index.html')

#crud
#c-create-add a record into db
def create_student(request):
    form=StudentForm()
    return render(request,'myapp/studentform.html',{'form':form})