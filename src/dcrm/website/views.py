from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def home_page_view(request):
    return render(request, 'home.html', {})

def login_user(request):
    pass

def logout_user(request):
    pass