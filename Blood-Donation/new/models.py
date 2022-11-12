from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Connect(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length = 20)
    age = models.IntegerField()
    group = models.CharField(max_length = 20)
    address =models.TextField(max_length = 200)
    mob = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    profile_image = models.ImageField(null=True, blank=True, upload_to="images/")
    status = models.CharField(max_length=10, null=True)
    role = models.CharField(max_length = 50)
    reason = models.CharField(max_length = 100)
    unit = models.IntegerField()


    def __str__(self):
        return self.name

class Donor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length = 20)
    age = models.IntegerField()
    group = models.CharField(max_length = 20)
    address =models.TextField(max_length = 200)
    mob = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    Lastdate = models.DateField(null=True)
    updated = models.DateTimeField(auto_now=True)
    profile_image = models.ImageField(null=True, blank=True, upload_to="images/")
    status = models.CharField(max_length=10, null=True)
    role = models.CharField(max_length = 50)
    desease = models.CharField(max_length = 100)
    unit = models.IntegerField()

    def __str__(self):
        return self.name


class Bloodbank(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    donorname = models.CharField(max_length = 20)
    age = models.IntegerField()
    group = models.CharField(max_length = 10)
    health = models.CharField(max_length = 50)
    date = models.DateTimeField(auto_now_add=True)
    duedate = models.DateField()
    reason = models.CharField(max_length = 50)
    status = models.CharField(max_length = 20)
    unitrequest = models.IntegerField()
    donorid = models.CharField(max_length = 3)

    def __str__(self):
        return self.donorname



    
    