from django.contrib import admin
from chat.models import Room, Message, Topic, User, Customer, Product, Order, OrderItem 
# Register your models here.

admin.site.register(Topic)
admin.site.register(Room)
admin.site.register(Message)
admin.site.register(User)
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)