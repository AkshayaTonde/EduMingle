from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import *

# Create your views here.
def home(request):
    return render(request, "Home/Index.html")

def friends(request):
    return render(request, "Home/Friends.html")

def signIn(request):
    
    #When data is saved 
    if request.method == "POST":
        data = request.POST
        
        """name = data.get('name')
        age = data.get('age')
        email = data.get('email')
        school = data.get('school')
        joiningdate = "10/11/2024"
        profilepicture = request.FILES.get('profilepic')"""

        print("We get data =",data)

        Student.objects.create(
            name = data.get('name'),
            age = data.get('age'),
            email = data.get('email'),
            school = data.get('school'),
            joiningdate = "2024-11-14",
            profilepicture = request.FILES.get('profilepic')
        )

        return redirect ("/")
    #when get method just to view webpage
    if request.method =="GET":
        return render(request, "Home/SignIn.html")
    


def contactUs(request):
    return render(request, "Home/Contact.html")

def viewAllStudents(request):
    queryset = Student.objects.all()
    context = {"allstudents": queryset}
    return render(request, "Home/allStudents.html", context=context)


