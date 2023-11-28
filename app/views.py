from django.shortcuts import render, redirect, get_object_or_404
from mechanicall.forms import ServiceRequestForm, TowRequestForm,MechanicForm, TowForm

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Mechanic, Tow, ServiceRequest
from django.http import HttpResponse
import json
import requests
import json
from requests.auth import HTTPBasicAuth
from datetime import datetime
import base64

class MpesaC2bCredential:
    consumer_key = 'bmsGqvG3XIC4fCPu1ITA6Yfi5AadWc0W'
    consumer_secret = 'ecit5wPC197ElfZO'
    api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'


class MpesaAccessToken:
    r = requests.get(MpesaC2bCredential.api_URL,
                     auth=HTTPBasicAuth(MpesaC2bCredential.consumer_key, MpesaC2bCredential.consumer_secret))
    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token["access_token"]


class LipanaMpesaPpassword:
    lipa_time = datetime.now().strftime('%Y%m%d%H%M%S')
    Business_short_code = "174379"
    OffSetValue = '0'
    passkey = 'bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919'

    data_to_encode = Business_short_code + passkey + lipa_time

    online_password = base64.b64encode(data_to_encode.encode())
    decode_password = online_password.decode('utf-8')
from .models import Mechanic,Tow,User
from mechanicall.credentials import MpesaAccessToken,LipanaMpesaPpassword,MpesaC2bCredential

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
    return redirect('mechanicProfile')

def success(request):
    return render(request,'success.html')

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

# stk
def pay(request):
    return render(request, 'pay.html')

def index2(request):
    return render(request,'index-2.html')


def token(request):
    consumer_key = 'bmsGqvG3XIC4fCPu1ITA6Yfi5AadWc0W'
    consumer_secret = 'ecit5wPC197ElfZO'
    api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'

    r = requests.get(api_URL, auth=HTTPBasicAuth(
        consumer_key, consumer_secret))
    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token["access_token"]

    return render(request, 'token.html', {"token": validated_mpesa_access_token})


def stk(request):
    if request.method == "POST":
        phone = request.POST['phone']
        amount = request.POST['amount']
        access_token = MpesaAccessToken.validated_mpesa_access_token
        api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
        headers = {"Authorization": "Bearer %s" % access_token}
        request_data = {
            "BusinessShortCode": LipanaMpesaPpassword.Business_short_code,
            "Password": LipanaMpesaPpassword.decode_password,
            "Timestamp": LipanaMpesaPpassword.lipa_time,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": amount,
            "PartyA": phone,
            "PartyB": LipanaMpesaPpassword.Business_short_code,
            "PhoneNumber": phone,
            "CallBackURL": "https://sandbox.safaricom.co.ke/mpesa/",
            "AccountReference": "Mechanicall",
            "TransactionDesc": "Service charges"
        }
        response = requests.post(api_url, json=request_data, headers=headers)

        response_data = response.json()  # Parse the JSON response

        # Check if the transaction was successful
        if response_data.get('ResponseCode') == '0':
            # Transaction successful, redirect to mechanic list
            messages.success(request, 'Payment successful!')
            return redirect('success')
        else:
            # Transaction failed, display an error message
            messages.error(request, f'Payment failed: {response_data.get("ResponseDescription")}')
            return redirect('index')

def mechanicProfile(request):
    if request.method == 'POST':
        firstname = request.POST['username']
        password = request.POST['password']
        user = Mechanic.objects.filter(firstname=firstname, password=password).first()

        if user:
            messages.success(request, 'Login successful!')
            return render(request, 'mechanics-profile.html', {'member': user})
        else:
            messages.error(request, 'Invalid username or password.')
            return render(request, 'login-mech.html')
    else:
        return render(request, 'login-mech.html')

def towProfile(request):
    if request.method == 'POST':
        companyname = request.POST['username']
        password = request.POST['password']
        user = Tow.objects.filter(companyname=companyname, password=password).first()

        if user:
            messages.success(request, 'Login successful!')
            return render(request, 'tow-profile.html', {'member': user})
        else:
            messages.error(request, 'Invalid username or password.')
            return render(request, 'login-tow.html')
    else:
        return render(request, 'login-tow.html')
def mechLogin(request):
    return render(request,'login-mech.html')

def about(request):
    return render(request,'about.html')

def services(request):
    return render(request,'services.html')

def towLogin(request):
    return render(request,'login-tow.html')

# Admin
def admin_panel(request):
    mechanics = Mechanic.objects.all()
    tows = Tow.objects.all()
    services = ServiceRequest.objects.all()

    mechanic_form = MechanicForm()
    tow_form = TowForm()

    if request.method == 'POST':
        if 'add_mechanic' in request.POST:
            mechanic_form = MechanicForm(request.POST)
            if mechanic_form.is_valid():
                mechanic_form.save()

        elif 'add_tow' in request.POST:
            tow_form = TowForm(request.POST)
            if tow_form.is_valid():
                tow_form.save()

    return render(request, 'admin_panel.html', {'mechanics': mechanics, 'tows': tows, 'mechanic_form': mechanic_form, 'tow_form': tow_form,'services':services})

def edit_mechanic(request, mechanic_id):
    mechanic = get_object_or_404(Mechanic, id=mechanic_id)

    if request.method == 'POST':
        # Update mechanic details based on the form data
        mechanic.firstname = request.POST['firstname']
        mechanic.lastname = request.POST['lastname']
        mechanic.email = request.POST['email']
        mechanic.phone = request.POST['phone']
        mechanic.location = request.POST['location']
        mechanic.specialisation = request.POST['specialisation']
        mechanic.carbrand = request.POST['carbrand']
        mechanic.save()

        return redirect('admin_panel')

    return render(request, 'edit_mechanic.html', {'mechanic': mechanic})

def delete_mechanic(request, mechanic_id):
    mechanic = get_object_or_404(Mechanic, id=mechanic_id)

    if request.method == 'POST':
        mechanic.delete()
        return redirect('admin_panel')

    return render(request, 'delete_mechanic.html', {'mechanic': mechanic})


# Views for Tow Trucks
def edit_tow(request, tow_id):
    tow = get_object_or_404(Tow, id=tow_id)

    if request.method == 'POST':
        # Update tow truck details based on the form data
        tow.companyname = request.POST['companyname']
        tow.email = request.POST['email']
        tow.phone = request.POST['phone']
        tow.location = request.POST['location']
        tow.save()

        return redirect('admin_panel')

    return render(request, 'edit_tow.html', {'tow': tow})

def delete_tow(request, tow_id):
    tow = get_object_or_404(Tow, id=tow_id)

    if request.method == 'POST':
        tow.delete()
        return redirect('admin_panel')

    return render(request, 'delete_tow.html', {'tow': tow})

def add_mechanic(request):
    if request.method == 'POST':
        form = MechanicForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_panel')
    else:
        form = MechanicForm()

    return render(request, 'add_mechanic.html', {'form': form})

def add_tow(request):
    if request.method == 'POST':
        form = TowForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_panel')
    else:
        form = TowForm()

    return render(request, 'add_tow.html', {'form': form})