from django.shortcuts import render,redirect
from app.models import New, Tab
from django.http import HttpResponse
from app.forms import submit

# Create your views here.

def hello(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def home(request):
     return HttpResponse("hello world")

def access(request):
    a = New.objects.all()
    return render(request,'view.html',{'context':a})

def random(request):
    data = Tab.objects.all()
    return render(request, 'add.html', {'data':data})

def form1(request):
    if request.method == 'POST':
        f = submit(request.POST)
        if f.is_valid():
            f.save()
        return redirect('random') 
    else:
        f = submit()
        return render(request, 'jump.html', {'data': f})
