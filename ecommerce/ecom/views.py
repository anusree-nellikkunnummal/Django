from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from ecom.models import Register, Brand, Category, Product, Services, Cart, Wishlist, Order
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login, logout, authenticate
from ecom import models
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required



# Create your views here.
def home(request):
    brands = Brand.objects.all()
    categories = Category.objects.all()
    services = Services.objects.all()
    context = {'brands':brands, 'categories':categories, 'services':services}      
    return render(request, 'home.html', context)


def payment(request):
    return render(request, 'payment.html')

def login(request):
    return render(request, 'login.html')

def single_item(request):
    return render(request, 'single_item.html')  

def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        password2 = request.POST.get('password2')
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'username already registered try another or login')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'email already registered try another or login')
                return redirect(register)
            
            else:
                user = User.objects.create_user(username=username, password=password, email=email)
                user.save()
                member = models.Register(name=name, username=username, email=email, password=password, password2=password2)
                member.save()
                messages.success(request, 'Registered successfully')
        else:
            messages.error(request, 'password doesnot match')
            return redirect('register')

        return redirect('login')
    else:
        return render(request, 'register.html')

def logs(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
      
        user = authenticate(username=username, password=password) 
        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
             
            messages.error(request, 'username or password incorrect')
            return redirect('login')
    else:
        return render(request, 'login.html', {})

def logout_user(request):
    logout(request)
    return redirect('home')

def watch_list(request):
    brands = Brand.objects.all()
    categories = Category.objects.all()
    list = zip(brands, categories)
    return render(request, 'base.html', {'list':list}) 

def brand_view(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    item = Product.objects.filter(brand__brand_name__icontains = q)
    return render(request, 'brand_item.html', {'item':item})

def category_view(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    item = Product.objects.filter(category__category_name__icontains = q)
    return render(request, 'category_item.html', {'item':item})

def service_view(request, id):
    item = Services.objects.filter(id=id)
    return render(request, 'service_item.html', {'item':item})

def popular_brand(request):
    item = Product.objects.all()
    return render(request, 'home.html', {'item':item})

def select_item(request, id):
    item = Product.objects.get(id=id)
    return render(request, 'select_item.html', {'i':item})

def faq(request):
    return render(request, 'faq.html')
   
def buyer_protection(request):
    return render(request, 'buyer_protection.html')


@login_required(redirect_field_name='logs')
def add_bag(request, id):
    if request.user:
        if request.method == 'POST':
            user = request.user
            item = Product.objects.get(pk=id)
            qnty =  request.POST.get('qty')
            carts = Cart(customer=user, product = item, qty = qnty, counter = '0')
            carts.save()
            products = Cart.objects.all()
            return redirect(request, 'cart.html', {'products':products})
        else:
            return render(request, 'select_item.html')
            
def add_wishlist(request, id):
    if request.user:
        user = request.user
        item = Product.objects.get(pk=id)   
        wishlists = Wishlist(customer=user, product = item)
        wishlists.save()
        return JsonResponse('Item was added', safe=False)

def wishlist(request):
    if request.user:
        user = request.user
        products = Cart.objects.filter(customer=user)
        return render(request, 'wishlist.html', {'products':products})

def cart(request):
    if request.user:
        user = request.user
        products = Cart.objects.filter(customer=user)
        return render(request, 'cart.html', {'products':products})

def place_order(request):
    if request.user:
        user = request.user
        carts = Cart.objects.filter(customer=user).values()
        for i in carts:
            qty = i['qty']
            id = i['id']
            p_id = i['product_id']
            products = Product.objects.filter(id=p_id).values()
            cartitem = Cart.objects.filter(product_id=p_id).values()
            for i in cartitem:
                cartid = i['id']
            for i in products:
                price = i['price']
                total = float(qty)*float(price)
                order = Order(customer=user,cart_id=cartid,total=total, counter='1')
                orders = Order.objects.all()
                return render(request, 'cart.html', {'orders':orders})
              
    else:
        return redirect('logs')
