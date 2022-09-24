
from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),
    path('dat', views.dat, name='dat'),
    path('info', views.info, name='info'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('update/<int:id>', views.update, name='update'),
   
]
