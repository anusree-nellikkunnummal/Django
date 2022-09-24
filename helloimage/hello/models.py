from django.db import models

# Create your models here.
class profilemodel(models.Model):
    name = models.CharField(max_length = 30, unique=True)
    age = models.IntegerField()
    address = models.CharField(max_length = 100)
    profession = models.CharField(max_length = 50)
    photo = models.ImageField(upload_to = 'images/')

    def __str__(self):
        return self.name

  