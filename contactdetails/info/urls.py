from django.urls import path
from info import views

urlpatterns = [
    
    path('', views.home, name='home'),
    path('collect', views.collect, name='collect'),
    path('contactlist', views.contactlist, name='contactlist'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('update/<int:id>', views.update, name='update')
    
]
