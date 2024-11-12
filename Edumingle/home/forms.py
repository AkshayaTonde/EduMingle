# forms.py
from django import forms
from django.contrib.auth.models import User
from .models import Student

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']  # Exclude email and username

class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['phone', 'user_bio', 'profilepicture']
