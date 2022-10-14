from django.urls import path
from new import views

urlpatterns = [

    path('', views.home, name='home'),
    path('register', views.register, name='register'),
    path('logs', views.logs, name='logs'),
    path('userprofile', views.userprofile, name='userprofile'),
    path('adminprofile', views.adminprofile, name='adminprofile'),
    path('usersprofile', views.usersprofile, name='usersprofile'),
    path('donorprofile', views.donorprofile, name='donorprofile'),
    path('admindonation', views.admindonation, name='admindonation'),
    path('adminrequest', views.adminrequest, name='adminrequest'),
] 