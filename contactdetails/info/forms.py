from django import forms
from django.forms import ModelForm
from .models import Numbers

class Numberform(forms.ModelForm):
    class Meta:
        model = Numbers
        fields = '__all__'