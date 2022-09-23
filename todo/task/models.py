from django.db import models

# Create your models here.

class Todo(models.Model):
    name = models.CharField(max_length = 20)
    task = models.CharField(max_length = 20)
    description = models.CharField(max_length = 60)
    duedate = models.DateField()

    def __str__(self):
        return self.name