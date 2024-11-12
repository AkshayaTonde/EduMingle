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
        phone = data.get("phone")
        profilepic = request.FILES.get("profilepic")


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

            # Create the Student profile linked to the user
            Student.objects.create(user=user,
                                   phone = phone,
                                   profilepicture= profilepic)

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

            # Redirect to profile page without passing user and student objects
            return redirect('myprofilepage')
            
        else:
            print("Invalid username or password")
            messages.error(request, "Invalid username or password.")
    
    # Get request
    else:
        return render(request, "Home/login.html")


# views.py
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserProfileForm, StudentProfileForm
from .models import Student

@login_required
def myprofilepage(request):
    user = request.user  # Get the logged-in user

    # Get or create the associated Student profile
    student, created = Student.objects.get_or_create(user=user)

    if request.method == 'POST':
        user_form = UserProfileForm(request.POST, instance=user)
        student_form = StudentProfileForm(request.POST, request.FILES, instance=student)
        
        if user_form.is_valid() and student_form.is_valid():
            user_form.save()
            student_form.save()
            messages.success(request, "Profile updated successfully!")
            return redirect('myprofilepage')  # Redirect to avoid form resubmission
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        user_form = UserProfileForm(instance=user)
        student_form = StudentProfileForm(instance=student)

    return render(request, 'Home/myprofilepage.html', {
        'user_form': user_form,
        'student_form': student_form,
        'user': user,
        'student': student,
    })



def register(request):
    return render(request, "Home/register.html")

def delete_all(request):
    Student.objects.all().delete()
    return render(request, "Home/deleteall.html")

