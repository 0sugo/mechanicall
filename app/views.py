from django.shortcuts import render, redirect, get_object_or_404
from mechanicall.forms import ServiceRequestForm, TowRequestForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .models import Mechanic,Tow,User


def index(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.filter(username=username, password=password).first()

        if user:
            messages.success(request, 'Login successful!')
            return render(request, 'index.html', {'member': user})
        else:
            messages.error(request, 'Invalid username or password.')
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        member = User(firstname=request.POST['firstname'],
                        lastname=request.POST['lastname'],
                        email=request.POST['email'],
                        username=request.POST['username'],
                        password=request.POST['password'])
        member.save()
        return redirect('/')
    else:
        return render(request, 'register.html')
def login(request):
    return render(request, 'sign-up.html')


def mechanic_list(request):
    mechanics = Mechanic.objects.all()

    if request.method == 'POST':
        location = request.POST.get('location', '')
        faulty_part = request.POST.get('faulty_part', '')
        print(f"Location: {location}, Faulty Part: {faulty_part}")

        mechanics = Mechanic.objects.filter(location=location, specialisation=faulty_part)

        form = ServiceRequestForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print("Form NOT valid")
    return render(request, 'mechanic-list.html', {'mechanics': mechanics})


def tow_list(request):
    tows = Tow.objects.all()
    form = TowRequestForm(request.POST)

    if request.method == 'POST':

        if form.is_valid():
            form.save()
            location = request.POST.get('location', '')
            destination = request.POST.get('destination', '')
            print(f"Location: {location},destination: {destination}")
            tows = Tow.objects.filter(location=location)
        else:
            print("Form not valid")
    return render(request, 'tow-list.html', {'tows': tows})


def toggle_mechanic_status(request, mechanic_id):
    mechanic = get_object_or_404(Mechanic, id=mechanic_id)
    mechanic.toggle_busy_status()
    return redirect('mechanic_list')


def toggle_tow_status(request, tow_id):
    tow = get_object_or_404(Tow, id=tow_id)
    tow.toggle_busy_status()
    return redirect('tow_list')

# views.py

def register(request):
    if request.method == 'POST':
        member = User(firstname=request.POST['firstname'],
                        lastname=request.POST['lastname'],
                        email=request.POST['email'],
                        username=request.POST['username'],
                        password=request.POST['password'])
        member.save()
        return redirect('/')
    else:
        return render(request, 'sign-up.html')


def login(request):
    return render(request, 'login.html')
