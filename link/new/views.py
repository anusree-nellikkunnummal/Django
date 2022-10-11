from django.shortcuts import render,redirect
from new.models import Connect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate
from new.forms import UserCreateForm, ConnectForm
from django.contrib.auth.models import User
from . import models



# Create your views here.

def home(request):
    return render(request, 'new/home.html')


def register(request):
    if request.method == 'POST':
        
        username = request.POST.get('username')
        email= request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        name = request.POST.get('name')
        age = request.POST.get('age')
        group = request.POST.get('group')
        address = request.POST.get('address')
        mob = request.POST.get('mob')
        date = request.POST.get('date')
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email)
                user.save()
                userdetail = models.Connect(user=user, name=name, age=age, group=group, address=address, mob=mob, date=date )
                userdetail.save()
        else:
            return redirect('register')  
              
        return redirect('profile')          
    else:
        
        return render(request, 'new/regs.html')


def logs(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login = auth_login(request, user)
            return redirect('userprofile')
    context = {}
    return render(request, 'new/logs.html', {})

def profile(request):
    profile = Connect.objects.all()
    return render(request, 'new/profile.html', {'profile':profile})

def profileform(request):
    if request.method == 'POST':
        form = ConnectForm(request.POST)
        if form.is_valid():
            form.save()
            profile = Connect.objects.all()
            return render(request, 'new/profile.html', {'profile':profile})
    else:
        form = ConnectForm()
        return render(request, 'new/registerdata.html', {'form':form})

def donate(request, id):
    data = Connect.objects.get(id=id)
    return render(request, 'new/donate.html', {'data':data})
    
def userprofile(request):
    if request.user:
        user = request.user
        data = Connect.objects.all().filter(user = user).values()
        print(data)
        for i in data:
            print(i)
            return render(request, 'new/singleuser.html', {'i':i})
        return render(request, 'new/singleuser.html')

    
