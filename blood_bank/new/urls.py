from django.urls import path
from new import views

urlpatterns = [

    path('', views.home, name='home'),
    path('register', views.register, name='register'),
    path('logs', views.logs, name='logs'),
    path('profile', views.profile, name='profile'),
]