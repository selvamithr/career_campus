from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import User, Resume

def landing_view(request):
    return render(request, 'core/landing.html')

def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request, 'core/login.html')

def register_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request, 'core/register.html')

@login_required
def dashboard_view(request):
    return render(request, 'core/dashboard.html')

def logout_user(request):
    logout(request)
    return redirect('landing')
