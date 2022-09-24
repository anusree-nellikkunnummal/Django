from django.shortcuts import render, redirect
from details.forms import Contactmodelform
from details.models import Contactmodel
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('hello')

def info(request):
    data = Contactmodel.objects.all()
    return render(request, 'list.html',{'data':data})

def dat(request):
    if request.method == 'POST':
        f = Contactmodelform(request.POST)
        if f.is_valid():
            f.save()
            return redirect('info')
    else: 
        f = Contactmodelform()
        return render(request, 'contact.html', {'f':f})
        
def delete(request, id):
    p = Contactmodel.objects.get(id = id)
    p.delete()
    return redirect('info')

def update(request, id):
    if request.method == 'POST':
        p = Contactmodel.objects.get(id = id)
        f = Contactmodelform(request.POST, instance = p)
        if f.is_valid():
            f.save()
            return redirect('info')
    else:
        p = Contactmodel.objects.get(id = id)
        f = Contactmodelform(instance = p)
        return render(request, 'contact.html', {'f':f})



        
        



