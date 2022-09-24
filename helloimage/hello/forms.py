from django import forms
from django.forms import ModelForm
from hello.models import profilemodel

class profileform(forms.ModelForm):
    class Meta:
        model = profilemodel
        fields = '__all__'