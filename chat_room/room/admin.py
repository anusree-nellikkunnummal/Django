from django.contrib import admin
from room.models import Room, Topic, Message

# Register your models here.
admin.site.register(Room)
admin.site.register(Topic)
admin.site.register(Message)
