from socket import fromshare
from django import forms
from django.forms import ModelForm
from room.models import Room

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = '__all__'