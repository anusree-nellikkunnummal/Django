from django.shortcuts import render,redirect
from padapp.forms import forum
from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(request,'index.html')

def hi(request):
    return HttpResponse('hi')

def employee(request):
    # if request.method == 'POST':
    #     form = forum(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('employee_info')
    # else:
        form = forum()
        return render(request, 'collect.html', {'form':form})

def employee_info(request):
    data = employeecollection.objects.all()
    return render(request, 'info.html',{'data':data})