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

# common registration here connecting User and Connect datas
def register(request):
    if request.method == 'POST':

        profile_pic = request.FILES['profile_pic']
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
        last_date = request.POST.get('last_date')
        status = '0'
        role = 'user'

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email)
                user.save()
                userdetail = models.Connect(user=user, name=name, age=age, group=group, address=address, mob=mob, date=date, profile_image=profile_pic, Lastdate=last_date, status=status, role=role)
                userdetail.save()
        else:
            return redirect('register')  
              
        return redirect('logs')           
    else:
        
        return render(request, 'new/regs.html')

# common login here
def logs(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        data = Connect.objects.all().values()
        print(data)
        for i in data:
            role = i['role']
       
        user = authenticate(request, username=username, password=password)
        print('============', role)
        if user is not None and role == 'user':
            auth_login(request, user)
            return redirect('userprofile')
        elif username == 'dell' and password == '1234':
            return render(request, 'new/admin/admin.html')
        else:
            pass

    context = {}
    return render(request, 'new/logs.html', {})

# single userpage view after each user login   
def userprofile(request):
    if request.user:
        user = request.user
        data = Connect.objects.all().filter(user = user).values()
        print(data)
        for i in data:
            print(i)
            return render(request, 'new/singleuser.html', {'i':i})
    return render(request, 'new/singleuser.html')

    
def adminprofile(request):
    return render(request, 'new/admin/admin.html') 

def usersprofile(request):
    return render(request, 'new/patient.html')

def donorprofile(request):
    return render(request, 'new/donor.html')

def adminrequest(request):
    return render(request, 'new/admin/admin_patient_request.html')
    
def admindonation(request):
    return render(request, 'new/admin/admin-donationinfo.html')