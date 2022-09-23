from django.shortcuts import render
from .models import Todo

# Create your views here.
def home(request):
    return render(request, 'task.html')

def data(request):
    if request.method == 'POST':
        tempname = request.POST['nameinput']
        temptask = request.POST['taskinput']
        tempdescription = request.POST['descriptioninput']
        tempdate = request.POST['dateinput']

        form = Todo(name = tempname, task = temptask, description = tempdescription, duedate = tempdate)
        form.save()
        data = Todo.objects.all()
        return render(request, 'task.html', {'data':data})
    else:
        return render(request, 'task.html')
    
def delete(request, id):
        d =  Todo.objects.get(id=id)
        d.delete()
        data = Todo.objects.all()
        return render(request, 'task.html',{'data':data})

def update(request, id):
    if request.method == 'POST':
        p = Todo.objects.get(id = id)
        p.name = request.POST['nameinput']
        p.task = request.POST['taskinput']
        p.description = request.POST['descriptioninput']
        p.duedate = request.POST['dateinput']

        form = Todo(name=p.name, task=p.task, description=p.description, duedate=p.duedate)
        form.save()
        data = Todo.objects.all()
        return render(request, 'task.html', {'data':data})

    else:
        f = Todo.objects.get(id = id)
        return render(request, 'task.html', {'f':f})