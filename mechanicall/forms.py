from django import forms
from app.models import ServiceRequest,TowRequest,Mechanic,Tow

class ServiceRequestForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ['location', 'faulty_part', 'description']

class TowRequestForm(forms.ModelForm):
    class Meta:
        model = TowRequest
        fields = ['location','destination']

class MechanicForm(forms.ModelForm):
    class Meta:
        model = Mechanic
        fields = ['firstname', 'lastname', 'email', 'phone', 'location', 'specialisation', 'carbrand', 'password']

class TowForm(forms.ModelForm):
    class Meta:
        model = Tow
        fields = ['companyname', 'email', 'password', 'phone', 'location']