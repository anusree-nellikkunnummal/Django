from django.contrib import admin
from .models import Staff, Student, logs, Attendance_student, Mark, Leave, Leave_staff

# Register your models here.
admin.site.register(Staff)
admin.site.register(Student)
admin.site.register(logs)
admin.site.register(Attendance_student)
admin.site.register(Mark)
admin.site.register(Leave)
admin.site.register(Leave_staff)