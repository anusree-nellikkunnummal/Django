from django.db import models

# Create your models here.

class employeecollection(models.Model):
    name = models.CharField(max_length = 20, unique = True)
    adress = models.CharField(max_length = 20, unique = True)
    school = models.CharField(max_length = 20, unique = True)
    datejoined = models.DateField(max_length = 20, unique=True)
    age = models.FloatField(max_length = 2)

    def __str__(self):
        return self.name