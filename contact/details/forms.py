from django import forms
from django.forms import ModelForm
from .models import Contactmodel

class Contactmodelform(forms.ModelForm):
    class Meta:
        model = Contactmodel
        fields = '__all__'