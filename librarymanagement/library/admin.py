from django.contrib import admin
from library.models import Student, Librarian, Category, Books, Book_Issue
# Register your models here.

admin.site.register(Student)
admin.site.register(Librarian)
admin.site.register(Category)
admin.site.register(Books)
admin.site.register(Book_Issue)



