from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from library.models import Student, Librarian, Category, Books
from library import models
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib import messages
# Create your views here.

def home(request):
    return render(request, 'home.html')



def register(request):
    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        username = request.POST.get('username')
        rollnumber = request.POST.get('rollnumber')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        mob = request.POST.get('mob')
        jdate = request.POST.get('jdate')
        edate = request.POST.get('edate')
        photo = request.FILES['p']
        role = 'student'
        status = '0'

        if password1 == password2:
            if  User.objects.filter(username=username).exists():
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password1)
                user.save()
                print(user)
                student = models.Student(user=user, fullname=fullname, rollnumber=rollnumber, number=mob, joindate = jdate, expirydate = edate, photo=photo,role=role, status=status)
                student.save()
                print(student)
        else:
            return redirect('register')

        return redirect('logs')

    else:

        return render(request, 'register.html')

def  logs(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if User.objects.filter(username = username).exists():
            user = User.objects.filter(username=username).values()
            for i in user:
                id = i['id']
            if Student.objects.filter(user_id = id).exists():
                st = Student.objects.filter(user_id = id).values()
                for i in st:
                    role = i['role']
                    status = i['status']
                user = authenticate(request, username=username, password=password)
                if user is not None and role == 'student' and status == '1':
                    auth_login(request, user)
                    return redirect('student_dashboard')

            elif username == 'anu' and password == '1234':
                return redirect('admin_dashboard')
            else:
                pass
        else:
            return redirect('logs')
                
    else:
        return render(request, 'login.html')


def admin_dashboard(request):
    return render(request, 'librarian/dashboard.html')

def student_dashboard(request):
    return render(request, 'student/dashboard.html')

def student_profile(request):
    if request.user:
        user = request.user
        data = Student.objects.get(user = user)
        return render(request, 'student/studentprofile.html', {'data':data})
    

def update_student_profile(request, pk):

    if request.method == 'POST':
        p = Student.objects.get(id=pk)
        p.fullname = request.POST.get('fullname')
        p.rollnumber = request.POST.get('rollnumber')
        p.number = request.POST.get('mob')
        p.photo = request.FILES['p']
        p.save()
        return redirect('student_profile')
    else:
        p = Student.objects.get(id=pk)
        return render(request,'student/profile_update.html', {'data':p})

def delete_student_profile(request, pk):
        p = Student.objects.get(id=pk)
        p.delete()
        return redirect('student_dashboard') 



def create_librarian_profile(request):
    if request.user:
        user = request.user
        if request.method == 'POST' and request.FILES['im']:
            fullname = request.POST.get('fullname')
            number = request.POST.get('mob')
            photo = request.FILES['im']
            librarian = models.Librarian(user=user, name=fullname, number=number, photo=photo)
            librarian.save()
            return redirect('librarian_profile')
     
       
           
def librarian_profile(request):
    if request.user:
        user = request.user
        if Librarian.objects.filter(user=user).exists():
            data = Librarian.objects.filter(user=user).values()
            for i in data:
                return render(request, 'librarian/librarianprofile.html', {'i':i})   
        else:
            return render(request, 'librarian/createprofile.html')
         
     
       
   

def update_librarian_profile(request, pk):

    if request.method == 'POST':
        p = Librarian.objects.get(id=pk)
        p.name = request.POST.get('fullname')
        p.number = request.POST.get('mob')
        p.photo = request.FILES['photo']
        p.save()
        return redirect('librarian_profile')
    else:
        p = Librarian.objects.get(id=pk)
        return render(request,'librarian/profile_update.html', {'data':p})

def delete_librarian_profile(request, pk):
        p = Librarian.objects.get(id=pk)
        p.delete()
        return redirect('librarian_dashboard') 

def create_book_category(request):
    if request.method == 'POST':
        category = request.POST.get('category')
        category = models.Category(category = category)
        category.save()
    
        return redirect('category_list')
    else:
        return render(request, 'librarian/createcategory.html')

def category_list(request):
    data = Category.objects.all().values()
    for i in data:
        print('-----category',i)
    return render(request, 'librarian/bookcategory.html', {'data':data})


def create_book(request, pk): 
        if request.method == 'POST':
            category = Category.objects.get(id = pk)
            print(category)
            title = request.POST.get('title')
            author = request.POST.get('author')
            pages = request.POST.get('pages')
            summary = request.POST.get('summary')
            photo = request.FILES['photo']
            books = models.Books(book_category=category, book_title = title, book_author=author, book_pages=pages, summary=summary, book_photo = photo )
            books.save()
            return redirect('book_list')

        else:
            return render(request, 'librarian/create_book.html')


def book_list(request):
    data = Books.objects.all()   
    return render(request, 'librarian/booklist.html', {'data':data})

def student_book_list(request):
    data = Books.objects.all()   
    return render(request, 'student/allbook.html', {'data':data})

def student_management(request):
    students = Student.objects.all()
    return render(request,'librarian/student_manage.html', {'students':students})

def approve_student(request, pk):
    student = Student.objects.get(id = pk)
    student.status = 1
    student.save()
    return redirect('student_management')

def student_reject(request, pk):
    student = Student.objects.get(id = pk)
    student.delete()
    return redirect('student_management')

def approved_students(request):
    students = Student.objects.all()
    return render(request, 'librarian/approved_student.html', {'students':students})

def book_borrow(request, pk):
    if request.user:
        user = request.user
        student = Student.objects.get(user=user)
        book = Books.objects.get(id = pk)
        messages.success(request, 'Profile details updated.')


def book_issue(request, pk):

    if request.user:
        user = request.user
        student = Student.objects.get(user=user)
        book = Books.objects.get(id = pk)
        print(book)
        if request.method == 'POST':
            issue_date= request.POST.get('issue_date')
            due_date=request.POST.get('due_date')
            returndate = request.POST.get('returndate')
            remarkissue = request.POST.get('remarkissue')
            remarkreturn = request.POST.get('remarkreturn')
            status = '0'
            book_issue = models.Book_Issue(student=student,book=book,issue_date=issue_date,due_date=due_date,date_returned=returndate,remark_on_issue=remarkissue,remark_on_return=remarkreturn,status=status)
            book_issue.save()
            return render(request, 'librarian/issued_returnedbook.html')
        else:
            return render(request, 'librarian/book_issue.html')