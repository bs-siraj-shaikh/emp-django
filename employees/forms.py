# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from .models import Employee

# class EmployeesRegistrationForm(UserCreationForm):
#     email=forms.EmailField(required=True)
#     phone_number=forms.CharField(required=True)
#     accept_terms=forms.BooleanField(required=True)
    
    
#     class Meta:
#         model=Employee
#         fields=['first_name','last_name','email','phone_number','password1','password2','accept_terms']
        
#     def clean_email(self):
#         email=self.cleaned_data.get('email')
#         if Employee.objects.filter(email=email).exists():
#             raise forms.ValidationError('Email Already exists')
#         return email
    
#     def clean_phone_number(self):
#         phone_number=self.cleaned_data.get('phone_number')
#         if Employee.objects.filter(phone_number=phone_number).exists():
#             raise forms.ValidationError('Phone number already exists')
#         return phone_number
    