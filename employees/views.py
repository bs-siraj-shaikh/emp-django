from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
# Create your views here.
from employees.models import Employee
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login as auth_login
# from emoployees.forms import EmployeesRegistrationForm
# from employees.forms import EmployeesRegistrationForm

def register_employee(request):    
    if request.method=="POST":
        first_name=request.POST.get('f_name')
        last_name=request.POST.get('l_name')
        phone_number=request.POST.get('pnum')
        email=request.POST.get('email')
        password=request.POST.get('pass1')
        confirm_pass=request.POST.get('pass2')
        
        qs=Employee.objects.create(first_name=first_name,last_name=last_name,phone_number=phone_number,email=email)
        # print(qs.Empuc)
        
        if qs:
            send_mail(
                'Welcome to the Company',
                f'Hello {first_name},\n\nWelcome to the company! We are excited to have you on board.',
                'mailtrap@demomailtrap.com',
                [email],
                fail_silently=False,
            )
            messages.success(request, 'Registration successful. Welcome to the company!')
            return redirect('/employees/show')
            # return render(request,'employee_list.html')
    else:
        return render(request, 'register.html')       

def login(request):
    if request.methods=='POST':
        username = request.POST.get('username')
        password=request.POST.get('pass1')
        
        employee=authenticate(request,username=username,password=password)
        if employee is not None:
            auth_login(request,user=employee)
            return redirect('employee/show')
        else:
            messages.error(request,'Invalid Login credentials')
    return render(request,'login.html')
            
def get_employee(request):
    qs=Employee.objects.all()
    result={
        'data':qs
    }
    return render(request,'employee_list.html',result)

def update_employee(request):
    if request.method=='PUT':
        first_name=request.PUT.get('f_name')
        last_name=request.PUT.get('l_name')
        phone_number=request.PUT.get('pnum')
        email=request.PUT.get('email')
        
        if 'pass' in request.PUT:
            password=request.PUT.get('pass')
        
    return 

def delete_employee(request,Empuc):
    qs=Employee.objects.filter(Empuc=Empuc).delete()
    if qs:
        return redirect('/show')
    