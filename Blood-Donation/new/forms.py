from new.models import Connect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm


class ConnectForm(forms.ModelForm):
    class Meta:
        model = Connect
        fields = '__all__'

class UserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
