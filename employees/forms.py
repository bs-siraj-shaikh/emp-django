from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Employee
from django.db import models

class EmployeesRegistrationForm(forms.ModelForm):
    email=forms.EmailField(required=True)
    phone_number=forms.CharField(required=True)
    accept_terms=forms.BooleanField(required=True,label='Accept Terms')
    
    
    class Meta:
        model=Employee
        fields=['first_name','last_name','email','phone_number','accept_terms']
        
    def clean_email(self):
        email=self.cleaned_data.get('email')
        if Employee.objects.filter(email=email).exists():
            raise forms.ValidationError('Email Already exists')
        return email
    
    def clean_phone_number(self):
        phone_number=self.cleaned_data.get('phone_number')
        if Employee.objects.filter(phone_number=phone_number).exists():
            raise forms.ValidationError('Phone number already exists')
        return phone_number

class PasswordResetForm(forms.Form):
    new_password = forms.CharField(widget=forms.PasswordInput, label='New Password')
    confirm_password = forms.CharField(widget=forms.PasswordInput, label='Confirm Password')

    def clean(self):
        cleaned_data = super().clean()
        new_password = cleaned_data.get("new_password")
        confirm_password = cleaned_data.get("confirm_password")

        if new_password and confirm_password and new_password != confirm_password:
            raise forms.ValidationError("Passwords do not match")


class EmployeeUpdateForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'phone_number', 'department', 'location', 'address']

    def __init__(self, *args, **kwargs):
        super(EmployeeUpdateForm, self).__init__(*args, **kwargs)



    