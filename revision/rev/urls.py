from django.urls import path
from rev import views

urlpatterns = [
    path('', views.home, name='home'),
    path('hello', views.hello, name='hello')
]