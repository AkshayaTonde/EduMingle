from django.db import models
from django.contrib.auth.models import *

# Create your models here.

class Student(models.Model):
    user =  models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    phone = models.IntegerField(unique = True)
    user_bio = models.CharField(max_length= 50, null= True)
    profilepicture = models.ImageField(upload_to="profilepictures", null=True, blank=True)
