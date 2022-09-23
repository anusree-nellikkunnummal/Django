from django.db import models

# Create your models here.
class New(models.Model):
    name = models.CharField(max_length = 9, unique = True)
    password = models.CharField(max_length = 15, unique= True)
    username = models.CharField(max_length = 8, unique = True)
    def __str__(self):
        return self.name

class Tab(models.Model):
    firstname = models.CharField(max_length = 20, unique = True)
    lastname = models.CharField(max_length = 20, unique = True)
    email = models.CharField(max_length = 15, unique = True)

    def __str__(self):
        return self.firstname

    