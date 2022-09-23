from django import forms
from django.forms import ModelForm
from .models import employeecollection

class forum(forms.ModelForm):
    class Meta:
        model = employeecollection
        fields = ['name', 'adress', 'school', 'age', 'datejoined']
