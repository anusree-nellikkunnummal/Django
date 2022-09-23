from django.urls import path
from padapp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('hello', views.hi, name = 'hi'),
    path('employee', views.employee, name='collect'),
    path('employee_info', views.employee_info, name='info'),

]