from socket import fromshare
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from bank.models import UserInfo
class Regform(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class userInfoForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = '__all__'
