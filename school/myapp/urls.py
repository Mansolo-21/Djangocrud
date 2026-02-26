from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('add/',views.create_student,name='add'),
    path('admindashboard/',views.admin,name='admin')
]
