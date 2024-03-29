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
    path('index', views.index2,name='index2'),
    path('mechanics-list/', views.mechanic_list, name='mechanic_list'),
    path('tow-list/', views.tow_list, name='tow_list'),
    path('toggle-mechanic-status/<int:mechanic_id>/', views.toggle_mechanic_status, name='toggle_mechanic_status'),
    path('toggle-tow-status/<int:tow_id>/', views.toggle_tow_status, name='toggle_tow_status'),
    path('login/', views.login, name='login'),
    path('services/', views.services, name='services'),
    path('about/', views.about, name='about'),
    path('mechlogin/', views.mechLogin, name='mechLogin'),
    path('towlogin/', views.towLogin, name='towLogin'),
    path('mechprofile/', views.mechanicProfile, name='mechanicProfile'),
    path('towprofile/', views.towProfile, name='towProfile'),
    path('success/', views.success, name='success'),
    path('pay/', views.pay,name='pay'),
    path('token/', views.token,name='token'),
    path('stk/', views.stk,name='stk'),
#     CRUD
    path('admin_panel/', views.admin_panel, name='admin_panel'),
    path('add_mechanic/', views.add_mechanic, name='add_mechanic'),
    path('edit_mechanic/<int:mechanic_id>/', views.edit_mechanic, name='edit_mechanic'),
    path('delete_mechanic/<int:mechanic_id>/', views.delete_mechanic, name='delete_mechanic'),
    path('add_tow/', views.add_tow, name='add_tow'),
    path('edit_tow/<int:tow_id>/', views.edit_tow, name='edit_tow'),
    path('delete_tow/<int:tow_id>/', views.delete_tow, name='delete_tow'),
]
 