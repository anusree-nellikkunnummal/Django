from django.shortcuts import render,redirect
from new.models import Connect 
from new.forms import ConnectForm
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def home(request):
    return render(request, 'new/home.html')

def profile(request):
    data = Connect.objects.all()
    return render(request, 'new/profile.html', {'data':data})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserCreationForm()
        return render(request, 'new/regs.html', {'form':form})

def logs(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login = auth_login(request, user)
            return render(request, 'new/profile.html')
    context = {}
    return render(request, 'new/logs.html', {})
