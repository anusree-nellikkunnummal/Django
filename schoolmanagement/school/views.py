from django.shortcuts import render, redirect
from . import  models
from .models import Staff,Student, logs, Attendance_student, Mark, Leave, Leave_staff
from django.contrib.auth.models import User

# Create your views here.

def home(request):
    return render(request, 'home.html')

def admins(request):
    return render(request, 'admins/dashboard.html')

def staff(request):
    return render(request, 'staff/dashboard.html')

def student(request):
    return render(request, 'student/dashboard.html')

def staff_profile(request):
    return render(request, 'staff/profile.html')

def log(request):
    return render(request, 'logs.html')

def staff_register(request):
    if request.method == 'POST':
        name = request.POST.get('fullname')
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        email = request.POST.get('email')
        contact = request.POST.get('mob')
        address = request.POST.get('address')
        dob = request.POST.get('dob')
        jdate = request.POST.get('jdate')
        salary = request.POST.get('salary')
        subject = request.POST.get('sub')
        status = '0'
        role = 'staff'
        log_data = models.logs(username=username, password=password1, role=role)
        log_data.save()
        log = logs.objects.filter(username=username).values()
        for i in log:
            log_id = i['id']
            print(log_id, 'hello log_id')
            staff = models.Staff(name = name, login_id_id = log_id, username=username, email=email, password1=password1, contact=contact, address=address, dob=dob, joindate=jdate, salary=salary, status=status, role=role, subject=subject )
            staff.save()
        return redirect('log')

    else:
        return render(request, 'staff/staff_register.html')

def student_register(request):
    if request.method == 'POST':
        name = request.POST.get('fullname')
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        email = request.POST.get('email')
        contact = request.POST.get('mob')
        address = request.POST.get('address')
        dob = request.POST.get('dob')
        gender = request.POST.get('gender')
        parent = request.POST.get('parent')
        jdate = request.POST.get('jdate')
        rollid= request.POST.get('rollid')
        cls= request.POST.get('class')
        section= request.POST.get('section')
        status = '0'
        role = 'student'
        if  logs.objects.filter(username=username). exists():
            pass
        else:
            login_data = models.logs(username=username, password=password1, role=role) 
            print(login_data)
            login_data.save()
            log = logs.objects.filter(username=username).values()
            print('log', log)
            for i in log:
                log_id = i['id']

            student = models.Student(name = name, login_id_id = log_id, email=email, contact=contact, address=address, dob=dob, joindate=jdate, gender=gender, parent=parent, rollid=rollid, clas=cls, section=section, status=status )
            student.save()
        return redirect('log')

    else:
        return render(request, 'student/student_register.html')

def log(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username,password)
        if logs.objects.filter(username = username, password=password ).exists(): 
            log = logs.objects.filter(username = username, password=password ).values() 
            for i in log:
                id = i['id']
                role = i['role']    
            if Student.objects.filter(login_id_id=id).exists():
                student = Student.objects.filter(login_id_id = id).values()
                for i in student:
                    status = i['status'] 
                
                    if student is not None and role == 'student' and status == '1':
                        return redirect('student')
            elif Staff.objects.filter(login_id_id = id).exists():
                staff = Staff.objects.filter(login_id_id = id).values()
                for i in staff:
                    status = i['status']

                    if staff is not None and role == 'staff' and status == '1':
                        return redirect('staff')    
            elif username == 'anusree' and password == '12345':
                return redirect('admins')
    else:
        context= {}
        return render(request, 'logs.html', context)

def student_profile(request):
        log = logs.objects.all()
        for i in log:
            log_id = i.id
            data = Student.objects.filter(login_id_id=log_id).values()
            for student in data:
                 print(student)
                  
                 return render(request, 'student/profile.html', {'data':student})
    
def staff_profile(request):
        log = logs.objects.all()
        for i in log:
            log_id = i.id   
            data = Staff.objects.filter(login_id_id=log_id).values()
            print(data)
            for staff in data:
                 print(staff)
                  
                 return render(request, 'staff/profile.html', {'data':staff})

def give_attendance(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        rollno = request.POST.get('rollno')
        cls = request.POST.get('class')
        section = request.POST.get('section')
        date = request.POST.get('date')
        status = '0'
        attendance_student = models.Attendance_student(name=name, rollid=rollno, cls=cls,section=section, date=date, status=status)
        attendance_student.save()
        return redirect('student')
    else:
        return render(request, 'student/attendance.html')
def view_attendance(request):
    atnd = Attendance_student.objects.all()
    return render(request, 'staff/view_attendance.html', {'datas':atnd})

def student_mark(request):
    pass


def give_mark(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        rollid = request.POST.get('rollid')
        clas = request.POST.get('class')
        section = request.POST.get('section')
        mark = request.POST.get('mark')
        remark = request.POST.get('remark')
        subject = request.POST.get('sub')
        marks = models.Mark(name=name, rollid=rollid, cls=clas, section=section, mark=mark, subject=subject, action=remark)
        marks.save()
        return redirect('staff')

    else:
        return render(request, 'staff/mark.html')

def view_mark(request):
    log = logs.objects.all()
    for i in log:
        id = i.id
        if Student.objects.filter(login_id_id=id).exists():
            st = Student.objects.filter(login_id_id=id).values()
            for i in st:
                rollid = i['rollid']
                mark = Mark.objects.filter(rollid=rollid).values()
                return render(request, 'student/mark.html', {'datas':mark})

def view_mark_atstaff(request):
    datas=Mark.objects.all()
    return render(request, 'staff/show_mark.html', {'datas':datas})

def view_mark_atadmin(request):
    datas=Mark.objects.all()
    return render(request, 'admins/mark.html', {'datas':datas})

def view_student_attendance_atadmin(request):
    atnd = Attendance_student.objects.all()
    return render(request, 'admins/attendance.html', {'datas':atnd})
def student_manage_admin(request):
    st = Student.objects.all()
    return render(request, 'admins/student_manage.html', {'datas':st})

def staff_manage_admin(request):
    st = Staff.objects.all()
    return render(request, 'admins/staff_manage.html', {'datas':st})

def leaveapply(request):
    if request.method == 'POST':
        log = logs.objects.all()
        for i in log:
            id = i.id
            
            name = Student.objects.get(login_id_id = id)
            rollid = request.POST.get('rollid')
            clas = request.POST.get('class')
            section = request.POST.get('section')
            startdate = request.POST.get('startdate')
            enddate = request.POST.get('enddate')
            reason = request.POST.get('reason')
            status = '0'
            leave = models.Leave(name=name, rollid=rollid, clas=clas, section=section, startdate=startdate, enddate=enddate, reason=reason, status=status)

            leave.save()
            return redirect('student')

    else:
        return render(request, 'student/leave.html')
    

def leaveapply_atstaff(request):
    
    if request.method == 'POST':
        log = logs.objects.all()
        for i in log:
            id = i.id
            name = Staff.objects.get(login_id_id = id)
            subject = request.POST.get('subject')
            startdate = request.POST.get('startdate')
            enddate = request.POST.get('enddate')
            reason = request.POST.get('reason')
            leave = models.Leave_staff(name=name,subject=subject, startdate=startdate, enddate=enddate, reason=reason)

            leave.save()
            return redirect('staff')

    else:
        return render(request, 'staff/leave.html')

def show_leave(request):
    leave = Leave.objects.all()
    return render(request, 'admins/show_leave.html', {'datas': leave})

def approve_leave(request, pk):
    student = Leave.objects.get(id = pk)
    student.status = 1
    student.save()
    return redirect('show_leave')

def reject_leave(request, pk):
    student = Leave.objects.get(id = pk)
    student.status = -1
    student.save()
    return redirect('show_leave')

def leave_status(request):
    log = logs.objects.all()
    for i in log:
        id = i.id
        datas = Leave.objects.get(name_id = id)
        return render(request, 'student/leavestatus.html', {'data':datas})

def approve_staff(request, pk):
    staff = Staff.objects.get(id = pk)
    staff.status = 1
    staff.save()
    return redirect('staff_manage')

def reject_staff(request, pk):
    staff = Staff.objects.get(id = pk)
    staff.status = -1
    staff.save()
    return redirect('staff_manage')

def approve_student(request, pk):
    student = Student.objects.get(id = pk)
    student.status = 1
    student.save()
    return redirect('student_manage')

def reject_student(request, pk):
    student = Student.objects.get(id = pk)
    student.status = -1
    student.save()
    return redirect('student_manage')
