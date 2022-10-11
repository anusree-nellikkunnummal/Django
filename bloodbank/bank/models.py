from django.db import models

# Create your models here.
class Bbankregistration(models.Model):
    fullname = models.CharField(max_length = 20)
    age = models.IntegerField()
    email = models.EmailField(max_length = 20)
    bgroup = models.CharField(max_length=20)
    contact = models.IntegerField()
    password = models.CharField(max_length = 20)

    def __str__(self):
        return self.fullname 

class UserInfo(models.Model):
    name = models.CharField(max_length = 20)
    age = models.IntegerField()
    mob = models.IntegerField()
    address=models.CharField(max_length = 100)
    mail = models.CharField(max_length = 20)
    bloodbgroup = models.CharField(max_length = 20)
    healthstatus = models.CharField(max_length = 1000)
    gender = models.CharField(max_length = 20)

    def __str__(self):
        return self.name
