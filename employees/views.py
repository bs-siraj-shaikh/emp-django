from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
# Create your views here.
from employees.models import Employee,PasswordResetToken
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from employees.forms import EmployeeUpdateForm,PasswordResetForm
from employees.models import Employee 
from employees.forms import EmployeesRegistrationForm
from datetime import datetime, timedelta
from django.contrib.auth.forms import AuthenticationForm
import secrets
from django.urls import reverse


def register_employee(request):    
    if request.method=="POST":
        first_name=request.POST.get('f_name')
        last_name=request.POST.get('l_name')
        phone_number=request.POST.get('pnum')
        email=request.POST.get('email')
        password=request.POST.get('pass1')
        confirm_pass=request.POST.get('pass2')
        accept_terms=request.POST.get('terms_TF')
        
        if not first_name:
            messages.error(request,'Please enter first name')
            return render(request,'register.html')
        
        if password!=confirm_pass:
            messages.error(request,'Password is not matched')
            return render(request, 'register.html') 
            
        # if messages:
        #     return redirect('register')
        
        
        qs=Employee.objects.create_user(first_name=first_name,last_name=last_name,phone_number=phone_number,email=email, password=password)
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


def login_emp(request):
    if request.method == 'POST':
        # import pdb;pdb.set_trace()
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                messages.success(request, 'Login successful.')
                return redirect('update_employee')  # Redirect to desired page after login
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    
    return render(request, 'login.html', {'form': form})
            
def get_employee(request):
    qs=Employee.objects.all()
    result={
        'data':qs
    }
    return render(request,'employee_list.html',result)

# @login_required
def update_employee(request):
    try:
        employee = request.user  # Retrieve the employee associated with the logged-in user
    except Employee.DoesNotExist:
        messages.error(request, 'Employee profile not found.')
        return redirect('login')  # Redirect to login page if employee profile is not found

    # import pdb;pdb.set_trace()
    if request.method == 'POST':
        data={
            'first_name': request.POST.get('f_name'),
            "last_name": request.POST.get('l_name'),
            "phone_number":request.POST.get('pnum'),
            'password':request.POST.get('pass1'),
            'department':request.POST.get('department'),
            'location':request.POST.get('location'),
            'address':request.POST.get('address'),   
        }
        # employee.(data=data)
        for field, value in data.items():
            setattr(employee, field, value)
        employee.save()
        
        
        messages.success(request, 'Employee information updated successfully.')
        return redirect('show_employees')
    data={
        'employee':employee,
    }
        
        
    return render(request, 'update_emp.html', data)

def password_reset(request):
    if request.method=='POST':
        email=request.POST.get('email')
        if email:
            token=generate_token()
            PasswordResetToken.objects.create(email=email,token=token)
            reset_url=create_reset_url(request,token)
            send_mail(
                'Password Reset',
                f'Here is the link to reset password{reset_url}',
                'mailtrap@demomailtrap.com',
                [email],
                fail_silently=False,
            )
            messages.success(request, 'Password reset email sent. Please check your inbox.')
            return redirect('/employees/login')
        else:
            messages.error(request,'Enter a valid email address')
    return render(request,'password_reset.html')

def password_reset_confirm(request, token):
    try:
        reset_token = PasswordResetToken.objects.get(token=token, expires_at__gt=datetime.now())
        # Proceed with password reset (e.g., show a form to reset the password)
        
    except PasswordResetToken.DoesNotExist:
        return HttpResponse('Invalid or expired token', status=400)
    if request.method == 'POST':
        
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')
        if not new_password or not confirm_password:
            messages.error(request, 'Please enter both fields.')
        elif new_password != confirm_password:
            messages.error(request, 'Passwords do not match.')
        else:
            # import pdb;pdb.set_trace()
            try:
                emp=request.user
                # import pdb;pdb.set_trace()
                
                user = Employee.objects.get(email=reset_token.email)
                user.set_password(new_password)
                user.save()
                reset_token.delete()  # Delete the token after successful reset
                messages.success(request, 'Your password has been successfully reset.')
                return redirect('/employees/login')  # Adjust this to your login URL
            except emp.DoesNotExist:
                messages.error(request, 'User not found')
            
        
        
    return render(request, 'password_reset_confirm.html', {'token': token})
   
   


def create_reset_url(request, token):
    reset_url = request.build_absolute_uri(reverse('password_reset_confirm', kwargs={'token': token}))
    return reset_url       


def generate_token():
    return secrets.token_urlsafe(16)

def delete_employee(request,Empuc):
    if request.method == 'POST':
        emp = Employee.objects.get(Empuc=Empuc) # Get the authenticated user
        emp.delete()
        messages.success(request, 'Your account has been deleted successfully.')
        return redirect('login')  # Redirect to login page after deletion
    
    return render(request, 'delete_emp.html')
    