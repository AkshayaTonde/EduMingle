from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import *
from django.contrib import messages
from .models import *
from datetime import date
from django.contrib.auth import *

# Create your views here.
def home(request):
    return render(request, "Home/Index.html")

def friends(request):
    return render(request, "Home/Friends.html")

def signUp(request):
    
    #When data is saved 
    if request.method == "POST":
        data = request.POST
        
        first_name = data.get('firstname')
        last_name = data.get('lastname')
        email = data.get('email')
        username=data.get("username")


        print("We get data =",data)

        if User.objects.filter(username = username):
            messages.error(request, "Username already exists")
            return render(request, "Home/signUp.html")
        else:
            user = User.objects.create(
                first_name = first_name,
                last_name = last_name,
                email = email,
                username=username,
                date_joined= date.today().strftime('%Y-%m-%d')
            )
            user.set_password(data.get("Password"))
            user.save()
            messages.success(request, "Account Created Successfully!")
            return redirect ("/login")
        
    #when get method just to view webpage
    if request.method =="GET":
        return render(request, "Home/signUp.html")
    


def contactUs(request):
    return render(request, "Home/Contact.html")

def viewAllStudents(request):
    
    return render(request, "Home/allStudents.html", context=context)


def login_page(request):

    
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        print(f'User name {username} and password = {password}')

        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            print("user authenticated successfully")
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect("/")  # redirect to the desired page after login
        else:
            print("Invalid username or password")
            messages.error(request, "Invalid username or password.")
    
    # Get request
    else:
        return render(request, "Home/login.html")


def register(request):
    return render(request, "Home/register.html")

def delete_all(request):
    Student.objects.all().delete()
    return render(request, "Home/deleteall.html")

