from django.contrib.auth.models import User
from django.shortcuts import redirect,render
from . import models
from .models import Connect

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        name = request.POST.get('name')
        age = request.POST.get('age')
        address = request.POST.get('address')
        mob = request.POST.get('mob')
        date = request.POST.get('date')
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password1)
                user.save()
                userdetails=models.Connect(name=name, age=age, address=address, mob=mob, date=date)
                userdetails.save()
        else:
            return redirect('register')
        return redirect('profile')
    else:
        return render(request, 'regs.html')

def profile(request):
    if request.user:
        user = request.user
        data = Connect.objects.all().filter(user=user).values
        for i in data:
            return render (request, 'user.html', {'i':i})
        return render(request, 'user.html')