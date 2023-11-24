from django import forms
from app.models import ServiceRequest,TowRequest

class ServiceRequestForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ['location', 'faulty_part', 'description']

class TowRequestForm(forms.ModelForm):
    class Meta:
        model = TowRequest
        fields = ['location','destination']