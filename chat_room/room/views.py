from django.shortcuts import render,redirect
from room.models import Room
from room.forms import RoomForm

# Create your views here.
def home(request):
    rooms = Room.objects.all()
    context = {'rooms':rooms}
    return render(request, 'room/home.html', context)

def room(request, pk):
    rooms = Room.objects.get(id = pk)
    context ={'rooms':rooms}
    return render(request, 'room/room.html', context)

def createroom(request):

    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = RoomForm()
        return render(request, 'room/createroomform.html',{'form':form})

def roomupdate(request, id):
    if request.method == 'POST':

        room = Room.objects.get(id=id)
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')
        

    else:
        room = Room.objects.get(id=id)
        form = RoomForm(instance=room)
        return render(request, 'room/createroomform.html',{'form':form})

