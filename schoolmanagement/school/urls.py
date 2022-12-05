from django.urls import path
from school import views

urlpatterns = [
    
    path('', views.home, name='home'),
    path('staff', views.staff, name='staff'),
    path('admins', views.admins, name='admins'),
    path('student', views.student, name='student'),
    path('staff_profile', views.staff_profile, name='staff_profile'),
    path('staff_register', views.staff_register, name='staff_register'),
    path('student_register', views.student_register, name='student_register'),
    path('log', views.log, name='log'),
    path('student_profile', views.student_profile, name='student_profile'),
    path('staff_profile', views.staff_profile, name='staff_profile'),
    path('give_attendance', views.give_attendance, name='give_attendance'),
    path('view_attendance', views.view_attendance, name='view_attendance'),
    path('give_mark', views.give_mark, name='give_mark'),
    path('view_mark', views.view_mark, name='view_mark'),
    path('view_mark_atstaff', views.view_mark_atstaff, name='view_mark_atstaff'),
    path('student_manage', views.student_manage_admin, name='student_manage'),
    path('staff_manage', views.staff_manage_admin, name='staff_manage'),
    path('view_mark_atadmin', views.view_mark_atadmin, name='view_mark_atadmin'),
    path('view_student_attendance_atadmin', views.view_student_attendance_atadmin, name='view_student_attendance_atadmin'),
    path('leaveapply', views.leaveapply, name='leaveapply'),
    path('leaveapply_atstaff', views.leaveapply_atstaff, name='leaveapply_atstaff'),
    path('show_leave', views.show_leave, name='show_leave'),
    path('approve_leave/<int:pk>', views.approve_leave, name='approve_leave'),
    path('reject_leave/<int:pk>', views.reject_leave, name='reject_leave'),
    path('leave_status', views.leave_status, name='leave_status'),
    path('approve_staff/<int:pk>', views.approve_staff, name='approve_staff'),
    path('reject_staff/<int:pk>', views.reject_staff, name='reject_staff'),
    path('approve_student/<int:pk>', views.approve_student, name='approve_student'),
    path('reject_student/<int:pk>', views.reject_student, name='reject_student'),

]