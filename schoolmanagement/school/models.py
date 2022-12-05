from django.db import models

class logs(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50, unique=True)
    role = models.CharField(max_length=50)
    def __str__(self):
        return self.username

# Create your models here.
class Staff(models.Model):
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    email = models.CharField(max_length=50, unique=True)
    contact = models.IntegerField()
    address = models.CharField(max_length=50)
    dob = models.DateField()
    password1 = models.CharField(max_length=50)
    joindate = models.DateField(auto_now=True)
    salary = models.IntegerField()
    role = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    login_id = models.OneToOneField(logs, on_delete=models.CASCADE )
    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    email = models.CharField(max_length=50, unique=True)
    contact = models.IntegerField()
    address = models.CharField(max_length=50)
    dob = models.DateField()
    gender = models.CharField(max_length=50)
    parent = models.CharField(max_length=50)
    password1 = models.CharField(max_length=50)
    joindate = models.DateField(auto_now=True)
    rollid = models.IntegerField()
    clas = models.CharField(max_length=50)
    section = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    login_id = models.OneToOneField(logs, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Attendance_student(models.Model):
    name = models.CharField(max_length=5)
    rollid = models.IntegerField()
    cls = models.CharField(max_length=5)
    section = models.CharField(max_length=5)
    date = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Mark(models.Model):
    name = models.CharField(max_length=5)
    rollid = models.IntegerField()
    cls = models.CharField(max_length=5)
    section = models.CharField(max_length=5)
    mark = models.IntegerField()
    subject = models.CharField(max_length=5)
    action = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Leave(models.Model):
    name = models.ForeignKey(Student, on_delete=models.CASCADE)
    startdate = models.DateField(auto_now=True)
    enddate = models.DateField(auto_now=True)
    rollid = models.IntegerField()
    clas = models.CharField(max_length=50)
    section = models.CharField(max_length=50)
    reason = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Leave_staff(models.Model):
    name = models.ForeignKey(Staff, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    startdate = models.DateField(auto_now=True)
    enddate = models.DateField(auto_now=True)
    reason = models.CharField(max_length=50)
    def __str__(self):
        return self.name

    