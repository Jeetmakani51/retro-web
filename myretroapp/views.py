from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!")
            return redirect('register_view')
        
        User.objects.create_user(
            username=username,
            password=password,
            email=email
        )
        messages.success(request, "registration successful")
        return redirect('login_view')
    return render(request, 'index.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect('home_view')
        else:
            messages.error(request, "Invalid username or password")
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect(login_view)

@login_required(login_url="login")
def home_view(request):
    return render(request, 'home.html')
