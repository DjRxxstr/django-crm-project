from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def home_page_view(request):
    #To check if logging in
    #If logging in -> request will be POST
    #If already logged in -> request will be GET

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "You Have Been Logged In!")
            return redirect('home-page-view')
        else:
            messages.success(request, "Wrong credentials entered" )
            return redirect('home-page-view')

    else:
        return render(request, 'home.html', {})

# def login_user(request):
#     pass

def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out...")
    return redirect('home-page-view')

def register_user(request):
    return render(request, 'register.html', {})