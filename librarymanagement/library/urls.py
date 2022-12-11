from django.urls import path
from library import views

urlpatterns = [
    
    path('', views.home, name='home'),
    path('register', views.register, name='register'),
    path('logs', views.logs, name='logs'),
    path('admin_dashboard', views.admin_dashboard, name='admin_dashboard'),
    path('student_dashboard', views.student_dashboard, name='student_dashboard'),
    path('student_profile', views.student_profile, name='student_profile'),
    path('update_student_profile/<int:pk>', views.update_student_profile, name='update_student_profile'),
    path('delete_student_profile/<int:pk>', views.delete_student_profile, name='delete_student_profile'),
    path('librarian_profile', views.librarian_profile, name='librarian_profile'),
    path('create_librarian_profile', views.create_librarian_profile, name='create_librarian_profile'),
    path('update_librarian_profile/<int:pk>', views.update_librarian_profile, name='update_librarian_profile'),
    path('delete_librarian_profile/<int:pk>', views.delete_librarian_profile, name='delete_librarian_profile'),
    path('category_list', views.category_list, name='category_list'),
    path('create_book_category', views.create_book_category, name='create_book_category'),
    path('book_list', views.book_list, name='book_list'),
    path('create_book/<int:pk>', views.create_book, name='create_book'),
    path('student_book_list', views.student_book_list, name='student_book_list'),
    path('student_management', views.student_management, name='student_management'),
    path('approve_student/<int:pk>', views.approve_student, name='approve_student'),
    path('student_reject/<int:pk>', views.student_reject, name='student_reject'),
    path('approved_students', views.approved_students, name='approved_students'),
    path('book_issue/<int:pk>', views.book_issue, name='book_issue'),

   
]   
