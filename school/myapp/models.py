from django.db import models

# Create your models here.
class Student(models.Model):
    firstname= models.CharField(max_length=21)
    lastname= models.CharField(max_length=21)
    age= models.IntegerField()
    course=models.CharField()
    email = models.EmailField(null=True, blank=True)
    
    def __str__(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old and does {self.course}'