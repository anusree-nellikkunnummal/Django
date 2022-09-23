from django import forms
from django.forms import ModelForm
from .models import Tab

class submit(forms.ModelForm):
    class Meta:
        model = Tab
        fields = ['firstname','lastname','email'] 