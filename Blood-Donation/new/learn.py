def register(request):
    if request.method == 'POST':                                            
        form = registerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            retrun redirect( 'home')
        return redirect('register')



    else:
        form = registerForm()
        return render(request, 'registerform.html',{'form':form})

from django import forms
from django.forms import ModelForm
from .models import Donor
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class regForm(models.ModelForm):
    class Meta:
        model = Donor
        fields = '__all__'
class Usercreateform(Usercreateform):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email']

# without form
def register(request):
    if request.method == 'POST':
        username= request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        candidatename = request.POST.get('candname')
        age=request.POST.get('age')

        if password1==password2:
            if User.objects.filter(username=username).exists():
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email)
                user.save()
                model = models.Donor(user=user, name=name, age=age)
                model.save()
                
        else:
            return redirect('register')
        return redirect('log')
    else:

        return render(reuqest,'register.html')

        
          

def log(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        if User.objects.filter(username=username).exists():
            user = User.objects.get(username=username).values()
            id = user['id']
            if Connect.objects.filter(user_id=id).exists():
                patient = Connect.objects.get(user_id=id).values()
                role = patient['role']
                status = patient['status']
                user = auth_login(request, username=username, password=password)
                if User is not None and role == 'user' and status=='1':
                    authenticate(request, user)
                    return redirect('patientdashboard')
            elif Donor.objects.filter(user_id=id).exists():
                donor = Donor.objects.get(user_id=id).values()
                role = donor['role']
                status = donor['status']
                user = auth_login(request, username=username, password=password)
                if user is not None and role == 'donor' and status == '1':
                    authenticate(request, user)
                    return redirect('donordashboard')
            elif username == 'dell' and password == '1234':
                return redirect('admindashboard')
            else:
                pass
        else:
            return redirect('logs')    

    context = {}
    return render(request, 'blood/logs.html', {})




    else:
        context = {}
        return render(request, 'log.html', {})



# hello login



    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        u = User.objects.filter(username=username).values()
        print(u)
        for t in u:
            id = t['id']
            print(t)
            
            if Connect.objects.filter(user_id=id).exists():
                data = Connect.objects.filter(user_id=id).values()
                print(data)
                for i in data:
                    role = i['role']
                    status = i['status']
                    print(i) 
                user = authenticate(request, username=username, password=password)
                if user is not None and role == 'user' and status == '1':
                    auth_login(request, user)
                    return redirect('patientdashboard')

        
                data = Connect.objects.filter(user_id=id).values()    
                content = Donor.objects.filter(user_id=id).values()
                for i in content:
                    roles = i['role']
                    statuss = i['status']
                    print(i)
                
                print(user)
                
                
                if user is not None and roles == 'donor' and statuss == '1':
                    auth_login(request, user)
                    return redirect('donordashboard')

                elif  username == 'dell' and password == '1234':
                    return redirect('admindashboard')
                else:
                    pass    
    context = {}
    return render(request, 'blood/logs.html', {})

def userprofile(request):
   if request.user:
        user=request.user 
        data = Donor.objects.filter(user=user).values()
        for i in data:
            return render(request, 'html', {'i':i})

       
def update(request, pk):
    if request.method == 'POST':
        p = Donor.objects.get(id=pk)
        p.username = request.POST.get('username')
        p.age = request.POST.get('age')
        p.edu = request.POST.get('edu')
        p.save()
        return redirect(donordashboard)


def updateform(request, pk):
    p = Donor.objects.get(id=pk)
    return render(request, 'html', {'p':p})
def approval(request, pk):
    p = Donor.objects.get(id=pk)
    p.status = 1
    p.save()
    return redirect('adminboard')
def delete(request, ):

       