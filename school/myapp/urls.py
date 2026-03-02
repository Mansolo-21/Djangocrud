from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.create_student, name='add'),
    path('students/', views.read_students, name='students'),
    path('delete/<int:id>/', views.delete_student, name='delete'),
    path('update/<int:id>/', views.update_student, name='update'),
    path('register/', views.register_user, name='register'),
    path('login/', views.login_user, name='login')
]
