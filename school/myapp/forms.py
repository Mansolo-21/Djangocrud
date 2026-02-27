from django import forms 
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student 
        fields = ['firstname', 'lastname', 'email','age', 'course']
        widgets = {
            'firstname': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Your First Name'
            }),
            'lastname': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Your Last Name'
            }),
            'age': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder':'Enter age'
            }),
            'course': forms.Select(
                choices=[
                    ('Fullstack', 'Fullstack'),
                    ('Cybersecurity', 'Cybersecurity'),
                    ('Data Science', 'Data Science'),
                    ('Artificial Intelligence', 'Artificial Intelligence'),
            ],
                attrs={'class': 'form-control', 'placeholder':'Enter course'}),
            'email': forms.EmailInput(attrs={'class':'form-control','placeholder': 'Enter email'})
        }