from django.db import models

# Create your models here.
class Contactmodel(models.Model):
    name = models.CharField(max_length = 50)
    address = models.CharField(max_length = 100)
    contactnumber = models.IntegerField()
    def __str__(self):
        return self.name 
