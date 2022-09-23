from django.urls import path
from app import views
urlpatterns = [
   
    path('index',views.hello,name='hello'),
    path('about',views.about, name='about'),
    path('access',views.access, name='access'),
    path('random', views.random, name= 'random'),
    path('', views.form1, name="form1")
    
]