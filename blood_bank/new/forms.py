from socket import fromshare
from django import forms
from django.forms  import ModelForm
from new.models import Connect

class ConnectForm(forms.ModelForm):
    class Meta:
        model = Connect
        fields = '__all__'

