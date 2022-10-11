
from django.urls import path
from bank import views

urlpatterns = [
   
    path('', views.home, name='home'),
    path('newform', views.newform, name='newform'),
    path('log', views.log, name='log'),
    path('userinfo', views.user_info, name='userinfo'),
    
  
   
] 
