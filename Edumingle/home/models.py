from django.db import models

# Create your models here.

class Student(models.Model):
    #id = models.AutoField()
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=15)
    email = models.EmailField()
    school = models.TextField()
    joiningdate = models.DateField()
    profilepicture = models.ImageField(upload_to="profilepictures", null=True, blank=True)
