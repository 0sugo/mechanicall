from django.shortcuts import render
from django.views.generic import ListView
from .models import Mechanic

# Create your views here.
def index(request):
    return render(request, 'index.html')

class MechanicListView(ListView):
    model = Mechanic
    template_name = 'mechanic-list.html'
    context_object_name = 'mechanics'
    # return render(request,'mechanic-list.html')