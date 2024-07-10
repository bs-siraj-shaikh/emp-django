from django.db import models
# from django.contrib.auth.models import BaseUserManager,AbstractBaseUser
# Create your models here.

# class EmployeeManager(BaseUserManager):
    
#     def create_user(self,email,password=None,**extra_fields):
#         if not email:
#             raise ValueError("The Email must be set")
#         email=self.normalize_email(email)
#         user=self.model(email=email,**extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

class Employee(models.Model):
    Empuc=models.AutoField(primary_key=True,serialize=True)
    email=models.EmailField(unique=True)
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30,blank=True,null=True)
    phone_number=models.CharField(max_length=10,unique=True)
    department=models.CharField(max_length=30,blank=True,null=True)
    location=models.CharField(max_length=100,blank=True,null=True)
    address=models.TextField(blank=True,null=True)
    
    class meta:
        db_table='Employee'
        
    USERNAME_FIELD="email","phone_number"
    
    
    