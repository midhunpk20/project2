from django.shortcuts import render,redirect
from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import *

def user_register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
    
        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return redirect('register_link')
        
        user = User.objects.create_user(
            username=username, 
            email=email, 
            password=password1)
        user.save()

    
        messages.success(request, "Account created successfully.")
        return redirect('login_link')

    return render(request, 'register.html')

def user_login(request):
    if request.method =="POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Logged in successfully.")
            return redirect('home_link')  # Replace 'home' with your desired redirect path
        else:
            messages.error(request, "Invalid credentials.")
    return render(request,'login.html')


def user_logout(request):
    logout(request)
    messages.success(request, "Logged out successfully.")
    return redirect('login_link')

def user_home(request):
    a= Contact.objects.all()

    return render(request,'home.html',{'user':a})


def user_contact(request):
    if request.method =="POST":
        a = request.POST.get("name")
        b = request.POST.get("address")
        c = request.POST.get("phone_number")
        d = request.POST.get("location")

        Contact.objects.create(

            name = a,
            address = b,
            phone_number = c,
            location = d

        )
        return redirect('home_link')
        
    return render(request,'contact.html') 


    
