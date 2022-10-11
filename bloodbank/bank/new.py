def home(request):
    return render(request, 'home.html')

def reg_data(request):
    data = Bbankregistration.objects.all()
    return render(request,'register.html', {'data':data})

def registration(request):
    if request.method == 'POST':
        tname = request.POST['name']
        tage = request.POST['age']
        tmail = request.POST['mail']
        tpassword = request.POST['password']
        tbgroup = request.POST['bgroup']
        tnum = request.POST['number']
        form = Bbankregistration(fullname=tname, age=tage, email=tmail, bgroup=tbgroup, contact=tnum, password=tpassword )
        form.save()
        return redirect('regdata')
    else: 
        return render(request, 'registrationform.html')