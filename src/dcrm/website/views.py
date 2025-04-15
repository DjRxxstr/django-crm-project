from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from .models import Record

def home_page_view(request):
    records = Record.objects.all()

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
        context = {
            'records' : records
        }
        return render(request, 'home.html', context)

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

def customer_record(request, id):
    if request.user.is_authenticated:
        customer_record = Record.objects.get(id = id)
        print(customer_record)

        context = {
            'customer_record' : customer_record
        }

        return render(request, 'record.html', context)

    else:
        messages.success(request, "You must be logged in to view records")
        return redirect('home-page-view')

def delete_record(request, id):
    if request.user.is_authenticated:
        delete_it = Record.objects.get(id = id)

        if request.method == 'POST':
            print(request.method)
            delete_it.delete()
            print(request.method)
            messages.success(request, "Record Deleted Successfully!")
            return redirect('home-page-view')

        context = {
            'customer_record' : delete_it
        }

        return render(request, 'delete.html', context)

    else:
        messages.success(request, "You must be logged in to delete records")
        return redirect('home-page-view')


def add_record(request):
    return render(request, 'add.html', {})