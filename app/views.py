from django.shortcuts import render, redirect
from mechanicall.forms import ServiceRequestForm,TowRequestForm
from .models import  Mechanic
from .models import Tow
def index(request):
    return render(request, 'index.html')

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

    if request.method=='POST':

        if form.is_valid():
            form.save()
            location = request.POST.get('location', '')
            destination = request.POST.get('destination', '')
            print(f"Location: {location},destination: {destination}")
            tows = Tow.objects.filter(location=location)
        else:
            print("Form not valid")
    return render(request, 'tow-list.html', {'tows':tows})