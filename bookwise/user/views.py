from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib import messages

from .forms import RegisterUserForm

def login_user(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Wrong password or username')

    return render(request, "login.html")

def logout_user(request):
    logout(request)
    return redirect('home')

def register_user(request):
    form = RegisterUserForm()
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            login(request, user)
            
            return redirect('home')
    
    return render(request, "register.html", {"form": form})