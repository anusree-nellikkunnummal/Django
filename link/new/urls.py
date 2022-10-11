from django.urls import path
from new import views

urlpatterns = [

    path('', views.home, name='home'),
    path('register', views.register, name='register'),
    path('logs', views.logs, name='logs'),
    path('profile', views.profile, name='profile'),
    path('profileform', views.profileform, name='profileform'),
    path('donate/<int:id>', views.donate, name='donate'),
    path('serprofile', views.userprofile, name='userprofile')
] 