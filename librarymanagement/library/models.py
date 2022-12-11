from django.db import models
from django.contrib.auth.models import User
from datetime import datetime,timedelta

# Create your models here.

class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=50)
    rollnumber = models.IntegerField(unique=True)
    number = models.IntegerField()
    photo = models.ImageField(upload_to= "images/", null=True, blank=True)
    role = models.CharField(max_length=50)
    status = models.CharField(max_length=10, null=True, blank=True)
    joindate = models.DateField()
    expirydate = models.DateField()
  
    def __str__(self):
        return self.fullname
        
class Librarian(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length = 30, unique=True)
    number = models.IntegerField()
    photo = models.ImageField(upload_to = 'images/')
    def __str__(self):
        return self.name


 
class Category(models.Model):
    category = models.CharField(max_length=50)
    def __str__(self):
        return self.category

class Books(models.Model):
    book_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    book_title = models.CharField(max_length=100)
    book_author = models.CharField(max_length=100)
    book_pages = models.IntegerField()
    summary=models.TextField(max_length=500, help_text="Summary about the book",null=True,blank=True)
    book_photo = models.ImageField(null=True, blank=True, upload_to = 'images/')
    def __str__(self):
        return self.book_title
def get_returndate():
    return datetime.today()+timedelta(days=8)

class Book_Issue(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    issue_date = models.DateTimeField(auto_now=True, help_text='Date the book is issued')
    due_date = models.DateTimeField(default=get_returndate(), help_text='Date the book is due to')
    date_returned = models.DateField(null=True, blank=True, help_text='Date the book is returned')
    remark_on_issue = models.CharField(max_length=100, default='Book in good condition', help_text='Book remarks/condition during issue')
    remark_on_return = models.CharField(max_length=100, default='Book in good condition', help_text='Book remarks/Condition during return')
    status = models.CharField(max_length=10, null=True, blank=True)
    def __str__(self):
        return self.student.fullname + 'Borrowed'+ self.book.book_title

