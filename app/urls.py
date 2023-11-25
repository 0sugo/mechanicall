"""
URL configuration for mechanicall project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views¬
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login,name='login'),
    path('register/', views.register,name='register'),
    path('', views.index,name='index'),
    path('mechanics-list/', views.mechanic_list, name='mechanic_list'),
    path('tow-list/', views.tow_list, name='tow_list'),
    path('toggle-mechanic-status/<int:mechanic_id>/', views.toggle_mechanic_status, name='toggle_mechanic_status'),
    path('toggle-tow-status/<int:tow_id>/', views.toggle_tow_status, name='toggle_tow_status'),
    path('login/', views.login, name='login'),
]
 