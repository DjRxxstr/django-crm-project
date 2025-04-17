from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, CustomerRecordForm
from .models import Record
from django.contrib.auth.models import Group
from .decorators import role_required
import csv
from django.http import HttpResponse


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


def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out...")
    return redirect('home-page-view')

def register_user(request):
    form = SignUpForm(request.POST or None)

    if form.is_valid():
        user = form.save(commit=False)  
        # Don't save so we can assign group

        role = form.cleaned_data['role']  
        # Get selected role

        user.save()  
        # Now save user after modifying

        # Assign user to selected group
        try:
            group = Group.objects.get(name=role.capitalize())
            user.groups.add(group)

        except Group.DoesNotExist:
            messages.error(request, f"The group '{role}' does not exist. Please create it in admin panel.")
            return redirect('register-user')

        # Log in the user
        username = form.cleaned_data['username']
        password = form.cleaned_data['password1']
        user = authenticate(username=username, password=password)
        login(request, user)

        messages.success(request, "You have Successfully Registered as " + role.capitalize() + "!")
        return redirect('home-page-view')

    context = {
        'form': form
    }

    return render(request, 'register.html', context)

@role_required(allowed_roles=['Admin', 'Staff', 'Viewer'])
def customer_record(request, id):
    if request.user.is_authenticated:
        customer_record = Record.objects.get(id = id)
        print(customer_record)

        context = {
            'customer_record' : customer_record
        }

        return render(request, 'record.html', context)

    # else:
    #     messages.success(request, "You must be logged in to view records")
    #     return redirect('home-page-view')

@role_required(allowed_roles=['Admin'])
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
            'customer_record' : delete_it,
            'fun' : 'delete'
        }

        return render(request, 'delete.html', context)

    # else:
    #     messages.success(request, "You must be logged in to delete records")
    #     return redirect('home-page-view')

@role_required(allowed_roles=['Admin', 'Staff'])
def add_record(request):
    form = CustomerRecordForm(request.POST or None)

    if request.user.is_authenticated:
        if form.is_valid():
            form.save()
            messages.success(request, "You have Successfully Added a Record!")
            print(form.cleaned_data)
            return redirect('add_record')

        context = {
            'form' : form,
            'fun' : 'add'
        }

        return render(request, 'add.html', context)

    # else:
    #     messages.success(request, "You must be logged in to delete records")
    #     return redirect('home-page-view')

@role_required(allowed_roles=['Admin', 'Staff'])
def update_record(request, id):
    if request.user.is_authenticated:
        record = Record.objects.get(id = id)

        form = CustomerRecordForm(request.POST or None, instance = record)

        if form.is_valid():
            form.save()
            print(form.cleaned_data)
            messages.success(request, "You have Successfully updated a Record!")
            return redirect('update_record', id=id)

        context = {
            'id' : id,
            'form' : form,
            'fun' : 'update'
        }

        return render(request, 'update.html', context)

    # else:
    #     messages.success(request, "You must be logged in to update records")
    #     return redirect('home-page-view')


@role_required(allowed_roles=['Admin'])
def export_csv(request):
    if request.user.is_authenticated:
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=customers.csv'

        writer = csv.writer(response)
        writer.writerow(['ID', 'First Name', 'Last Name', 'Email', 'Phone', 'Address', 'City', 'State', 'Zipcode', 'Created At'])

        from .models import Record
        records = Record.objects.all()

        for record in records:
            writer.writerow([
                record.id,
                record.first_name,
                record.last_name,
                record.email,
                record.phone,
                record.address,
                record.city,
                record.state,
                record.zipcode,
                record.created_at.strftime("%Y-%m-%d %H:%M")
            ])

        return response

