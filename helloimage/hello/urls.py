
from django.urls import path
from hello import views

urlpatterns = [
    
    path('', views.home, name='home'),
    path('profiledata', views.profile_data, name='profiledata'),
    path('profilelogin', views.profile_login, name='login')
]
