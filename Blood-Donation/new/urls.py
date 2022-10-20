from django.urls import path
from new import views

urlpatterns = [

    path('', views.home, name='home'),
    path('register', views.register, name='register'),
    path('logs', views.logs, name='logs'),
    path('userprofile', views.userprofile, name='userprofile'),
    # path('adminprofile', views.adminprofile, name='adminprofile'),
    # path('usersprofile', views.usersprofile, name='usersprofile'),
    path('donordashboard', views.donor_dashboard, name='donordashboard'),
    path('admindashboard', views.admin_dashboard, name='admindashboard'),
    path('patientdashboard', views.patient_dashboard, name='patientdashboard'),
    path('admindonation', views.admindonation, name='admindonation'),
    path('adminrequest', views.adminrequest, name='adminrequest'),
    path('donorregister', views.donor_register, name='donorregister'),
    path('donorprofile', views.donor_profile, name='donorprofile'),
    path('usermakerequest', views.usermakerequest, name='usermakerequest'),
    path('userrequesthistory', views.userrequesthistory, name='userrequesthistory'),
    path('donordata', views.donordata, name='donordata'),
    path('donorapproval/<int:register_id>', views.donorapproval, name='donorapproval'),
    path('approveddonor', views.approveddonor, name='approveddonor'),
    path('rejectdonor/<int:register_id>', views.rejectdonor, name='rejectdonor'),
    path('patientrequest', views.patientrequest, name='patientrequest'),
    path('removepatient/<int:register_id>', views.removepatient, name='removepatient'),
    path('patientapproval/<int:register_id>', views.patientapproval, name='patientapproval'),
    path('approvedpatient', views.approvedpatient, name='approvedpatient'),
    
    
    

    

] 