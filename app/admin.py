from django.contrib import admin
from .models import Mechanic,ServiceRequest,Tow,TowRequest,User
# Register your models here.

admin.site.register(Mechanic)
admin.site.register(Tow)
admin.site.register(ServiceRequest)
admin.site.register(TowRequest)
admin.site.register(User)
