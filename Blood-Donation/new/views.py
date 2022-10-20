from django.shortcuts import render,redirect
from new.models import Connect, Donor
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate
from new.forms import UserCreateForm, ConnectForm
from django.contrib.auth.models import User
from . import models



# Create your views here.

def home(request):
    return render(request, 'blood/home.html')

# common registration here connecting User and Connect datas
def register(request):
    if request.method == 'POST':

        profile_pic = request.FILES['profile_pic']
        username = request.POST.get('username')
        email= request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        name = request.POST.get('name')
        age = request.POST.get('age')
        group = request.POST.get('group')
        address = request.POST.get('address')
        mob = request.POST.get('mob')
        date = request.POST.get('date')
        reason=request.POST.get('reason')
        unit = request.POST.get('unit')
        updated = request.POST.get('updated')
        status = '0'
        role = 'user'

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email)
                user.save()
                userdetail = models.Connect(user=user, name=name, age=age, group=group, address=address, mob=mob, date=date, profile_image=profile_pic, reason=reason, unit=unit, status=status, role=role)
                userdetail.save()
        else:
            return redirect('register')  
              
        return redirect('logs')           
    else:
        
        return render(request, 'patient/regs.html')

# common login here
def logs(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        data = Connect.objects.all().values()
        print(data)
        for i in data:
            role = i['role']
            status = i['status']
        content = Donor.objects.all().values()
        print(content)
        for i in content:
            role = i['role']
            status = i['status']
       
        user = authenticate(request, username=username, password=password)
        if user is not None and role == 'user' and status == '1':
            auth_login(request, user)
            return redirect(request, 'patientdashboard')
        elif username == 'dell' and password == '1234':
            return redirect('admindashboard')
        elif user is not None and role == 'donor' and status == '1':
            auth_login(request, user)
            return redirect('donordashboard')
        else:
            pass

    context = {}
    return render(request, 'blood/logs.html', {})

# single userpage view after each user login   
def userprofile(request):
    if request.user:
        user = request.user
        data = Connect.objects.all().filter(user = user).values()
        print(data)
        for i in data:
            print(i)
            return render(request, 'patient/userprofile.html', {'i':i})
    return render(request, 'patient/userprofile.html')

    
def userrequesthistory(request):
    return render(request, 'patient/makerequest.html') 

def usermakerequest(request):
    return render(request, 'patient/patientrequest.html')

def donor_dashboard(request):
    return render(request, 'donor/donor.html')

def adminrequest(request):
    return render(request, 'admin/admin_patient_request.html')
    
def admindonation(request):
    return render(request, 'admin/admin-donationinfo.html')

def admin_dashboard(request):
    return render(request, 'admin/admin.html')

def patient_dashboard(request):
    return render(request, 'patient/patient.html')


# Donor registration view -------->

def donor_register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        email = request.POST.get('email')
        password2 = request.POST.get('password2')
        name = request.POST.get('name')
        age = request.POST.get('age')
        group = request.POST.get('group')
        address = request.POST.get('address')
        mob = request.POST.get('mob')
        date = request.POST.get('date')
        last_date = request.POST.get('last_date')
        desease = request.POST.get('desease')
        unit = request.POST.get('unit')
        profile_pic = request.FILES['profile_pic']
        updated = request.POST.get('updated')
        status = 0
        role = 'donor'

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                return redirect('donorregister')
            elif User.objects.filter(email=email).exists():
                return redirect('donorregister')
            else:
                user = User.objects.create_user(username=username, email=email, password=password1)
                user.save()
                userdetail = models.Donor(user=user, name=name, age=age, group=group, address=address, mob=mob, date=date, profile_image=profile_pic, Lastdate=last_date, desease=desease, updated=updated, unit=unit, status=status, role=role)
                userdetail.save()
        else:
            return redirect('donorregister')  
              
        return redirect('logs')           
    else:
        
        return render(request, 'donor/donor_regs.html')
    
        

def donor_profile(request):
    if request.user:
        donor = request.user
        data = Donor.objects.all().filter(user=donor).values()
        print(data)
        for i in data:
            print(i)
            return render(request, 'donor/donorprofile.html', {'i':i})
        return render(request, 'donor/donorprofile.html')
            
def donordata(request):
    donation = Donor.objects.all()
    print()
    return render(request, 'admin/admin-donationinfo.html', {'donation':donation}) 

def donorapproval(request, register_id):
    d = Donor.objects.get(id=register_id)
    d.status = 1
    d.save()
    return redirect('donordata')

def approveddonor(request):
    d =  Donor.objects.all()
    return render(request, 'admin/approveddonor.html', {'d':d})

def rejectdonor(request, register_id):
    d = Donor.objects.get(id=register_id)
    d.delete()
    return render(request, 'admin/admin-donationinfo.html')

def patientrequest(request):
    data = Connect.objects.all()
    return render(request, 'admin/admin_patient_request.html',{'data':data})

def removepatient(request, register_id):
    d = Connect.objects.get(id=register_id)
    d.delete()
    data = Connect.objects.all()
    return render(request, 'admin/admin_patient_request.html',{'data':data})

def patientapproval(request, register_id):
    d = Connect.objects.get(id=register_id)
    d.status = 1
    d.save()
    data =  Connect.objects.all()
    return redirect(request, 'admin/admin_patient_request.html', {'data':data})

def approvedpatient(request):
    data = Connect.objects.all()
    return render(request, 'admin/approvedpatient.html', {"data":data})
    


