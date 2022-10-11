from django.urls import path
from room import views

urlpatterns = [
    path('', views.home, name='home'),
    path('room/<str:pk>', views.room, name='room'),
    path('createroom', views.createroom, name='createroom'),
    path('roomupdate/<int:id>', views.roomupdate, name='roomupdate'),
    ]