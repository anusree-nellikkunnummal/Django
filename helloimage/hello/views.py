from django.shortcuts import render,redirect
from django.http import HttpResponse
from hello.models import profilemodel
from hello.forms import profileform

# Create your views here.
def home(request):
    return HttpResponse('Hello profiles')

def profile_data(request):
    data = profilemodel.objects.all()
    return render(request,'profile_data.html', {'data':data})

def profile_login(request):
    if request.method == 'POST':
        form = profileform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('profiledata')
    else:
        form = profileform()
    return render(request, 'login.html',{'form':form})

