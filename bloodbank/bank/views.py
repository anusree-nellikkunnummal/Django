from django.shortcuts import render, redirect
from bank.models import Bbankregistration, UserInfo
from bank.forms import Regform
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login


# Create your views here.
def home(request):
    return render(request, 'home.html')

def newform(request):
    if request.method == 'POST':
        form = Regform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('log')
        
    else:
        form = Regform()
        return render(request, 'registrationform.html', {'form':form})

def log(request):
    if request.method == 'POST':
        tuser = request.POST.get('username')
        tpas = request.POST.get('password')
        user = authenticate(request, username=tuser, password=tpas)
        if user is not None:
            auth_login(request,user)
            data = Bbankregistration.objects.all()
            return render(request,'donor.html',{'data':data} )
    context = {}
    return render(request, 'loginform.html', {})

def user_info(request):
    data = UserInfo.objects.all()
    return render(request, 'user.html', {'data':data})






