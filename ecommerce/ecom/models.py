from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Register(models.Model):
    name = models.CharField(max_length=20)
    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField(max_length=20, unique=True)
    password = models.CharField(max_length=20, unique=True)
    password2 =models.CharField(max_length=20, unique=True)
    def __str__(self):
        return self.name

class Services(models.Model) :
    services = models.CharField(max_length=100)
    def __str__(self):
        return self.services

class Category(models.Model):
    category_name = models.CharField(max_length=100)
    def __str__(self):
        return self.category_name

class Brand(models.Model):
    brand_name = models.CharField(max_length=100)
    def __str__(self):
        return self.brand_name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    model_name = models.CharField(max_length=100)
    price = models.FloatField()
    photo = models.ImageField(upload_to='images')
    subimage1 = models.ImageField(upload_to='images')
    subimage2 = models.ImageField(upload_to='images')
    subimage3 = models.ImageField(upload_to='images')
    subimage4 = models.ImageField(upload_to='images')
    emi = models.IntegerField()
    description = models.TextField()
    discount = models.IntegerField()
    def __str__(self):
        return self.category.category_name + self.brand.brand_name

   
class Cart(models.Model):
    customer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    qty = models.CharField(max_length=100)
    counter = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    
class Wishlist(models.Model):
    customer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    



        




    


