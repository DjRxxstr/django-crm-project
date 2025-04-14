from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm

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
    form = SignUpForm(request.POST or None)

    if form.is_valid():
        form.save()

        username = form.cleaned_data['username']
        password = form.cleaned_data['password1']
        user = authenticate(username=username, password=password)
        login(request, user)
        messages.success(request, "You have Successfully Registered!")
        return redirect('home-page-view')

    context = {
        'form' : form
    }

    return render(request, 'register.html', context)

    # if request.method == 'POST':
    #     form = SignUpForm(request.POST or None)

    #     if form.is_valid():
    #         form.save()

    #         username = form.cleaned_data['username']
    #         password = form.cleaned_data['password']
    #         user = authenticate(username=username, password=password)
    #         login(request, user)
    #         messages.success(request, "You have Successfully Registered!")
    #         return redirect('home-page-view')

    # else:
    #     form = SignUpForm() #Default request is 'GET'
    #     context = {
    #         'form' : form
    #     }
    #     return render(request, 'register.html', context)
        
    # return render(request, 'register.html', context)