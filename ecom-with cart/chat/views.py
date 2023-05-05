from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from chat.forms import RoomForm
from django.db.models import Q 
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import RoomForm, UserForm, MyUserCreationForm



# Create your views here.

def loginpage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = User.objects.get(email=email)
        except:
            messages.error(request, 'User does not exist')
      
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username or password does not exist')

    
    return render(request, 'login_register.html', {'page':page})

def logoutuser(request):
    logout(request)
    return redirect('home')

def registerpage(request):
    form = MyUserCreationForm()
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
           user = form.save(commit=False)
           user.username = user.username.lower()
           user.save()
           login(request, user)
           return redirect('home')
    messages.error(request, 'An error occured during registration')
 
    return render(request, 'login_register.html',{'form':form })

def home(request):
    q = request.GET.get('q') if request.GET.get('q')!= None else ''
    rooms = Room.objects.filter(
        Q(topic__name__icontains=q)|
        Q(name__icontains=q)|
        Q(description__icontains=q)
    )

    room_count = rooms.count()
    topics = Topic.objects.all()
    room_messages = Message.objects.filter(Q(room__topic__name__icontains=q))
    context = {'rooms': rooms, 'topics':topics, 'room_count':room_count, 'room_messages':room_messages}
    return render(request, 'home.html', context) 
 
def room(request,pk):
    room = Room.objects.get(id=pk)
    room_messages = room.message_set.all().order_by('-created')
    if request.method == 'POST':
        Message.objects.create(
        user=request.user,
        room=room,
        body=request.POST.get('body')
        )
        room.participants.add(request.user)
        return redirect('room', pk=room.id)
    context = {'room':room, 'room_messages':room_messages}
    return render(request, 'room.html', context)

def userprofile(request,pk):
    user = User.objects.get(id=pk)
    rooms = user.room_set.all()
    topics = Topic.objects.all()
    room_messages = user.message_set.all()
    context = {'user':user, 'rooms':rooms, 'topics':topics, 'room_messages':room_messages}
    return render(request, 'profile.html', context)

@login_required(login_url='login')
def createroom(request):
    form = RoomForm()
    topics = Topic.objects.all()
    if request.method == 'POST':
        topic_name = request.POST.get('topic')
        topic,created = Topic.objects.get_or_create(name=topic_name)
        Room.objects.create(
            host=request.user,
            topic=topic,
            name=request.POST.get('name'),
            description=request.POST.get('description'),

        )
        return redirect('home')

    context = {'form':form, 'topics':topics}
    return render(request, 'roomform.html', context) 

@login_required(login_url='login')
def updateroom(request, pk):
    room = Room.objects.get(id=pk)
    topics = Topic.objects.all()
    topic, created = Topic.objects.get_or_create(name='topic_name')
    if request.user != room.host:
        return HttpResponse('You are not allowed here!!')

    if request.method == 'POST':
        Room.objects.create(
        host=request.user,
        topic=topic,
        name=request.POST.get('name'),
        description=request.POST.get('description'),
    )
        return redirect('home')
    
    context = {'room': room, 'topic':topic}
    return render(request, 'roomform.html', context)
@login_required(login_url='login')
def deleteroom(request, pk):
    room = Room.objects.get(id=pk)

    if request.user != room.host:
        return HttpResponse('You are not allowed here!!')
    if request.method == 'POST':
        room.delete()
        return redirect('home')

    return render(request, 'deleteform.html', {'obj':room})

def deletemessage(request,pk):
    message = Message.objects.get(id=pk)
    
    if request.method == 'POST':
        message.delete()
        return redirect('home')
    
    return render(request, 'deleteform.html', {'obj':message})

@login_required(login_url='login')
def updateUser(request):
    user =request.user
    form = UserForm(instance=user)

    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('userprofile', pk=user.id)
    return render(request, 'update-user.html', {'form':form})

def topicspage(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    topics = Topic.objects.filter(Q(name__icontains=q))
    context = {'topics':topics}
    return render(request, 'topics.html', context)

def activitypage(request):
    room_messages = Message.objects.all()
    return render(request, 'activity.html', {'room_messages':room_messages})

def store(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request, 'home.html', context)

def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        print(customer)
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}
        
    context = {'items':items, 'order': order}
    return render(request, 'store/cart.html', context)


def checkout(request):
	context = {}
	return render(request, 'store/checkout.html', context)