from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import Numberform
from info.models import Numbers

# Create your views here.

def home(request):
    return HttpResponse('hello home')

def collect(request):
    if request.method == 'POST':
        form = Numberform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contactlist')
    else:
        form = Numberform()
        return render(request,'contact.html', {'form':form})

def contactlist(request):
    data = Numbers.objects.all()
    return render(request, 'listing.html', {'data':data})

def delete(request, id):
    p = Numbers.objects.get(id = id)
    p.delete()
    return redirect('contactlist')

def update(request, id):
    if request.method == 'POST':
        p = Numbers.objects.get(id = id)
        form = Numberform(request.POST, instance = p)
        if form.is_valid():
            form.save()
            return redirect('contactlist')
    else:
        p = Numbers.objects.get(id=id)
        form = Numberform(instance=p)
        return render(request, 'contact.html', {'form':form})
