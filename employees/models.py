from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser, AbstractUser, PermissionsMixin
from employees.managers import CustomUserManager
from datetime import datetime, timedelta

# Create your models here.

class Employee(AbstractBaseUser, PermissionsMixin):
    # user=models.OneToOneField(User,on_delete=models.CASCADE)
    Empuc=models.AutoField(primary_key=True)
    email=models.EmailField(unique=True)
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30,blank=True,null=True)
    phone_number=models.CharField(max_length=10,unique=True)
    department=models.CharField(max_length=30,blank=True,null=True)
    location=models.CharField(max_length=100,blank=True,null=True)
    address=models.TextField(blank=True,null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    
        
    USERNAME_FIELD="email"
    REQUIRED_FIELDS = ["first_name","phone_number"]
    
    objects = CustomUserManager()
    
    class meta:
        db_table='Employee'
    
        
    def update_employee(self, data):
        for field, value in data.items():
            if hasattr(self, field):
                setattr(self, field, value)
        self.save()
    
class PasswordResetToken(models.Model):
    email = models.EmailField()
    token = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()

    def save(self, *args, **kwargs):
        if not self.id:
            self.expires_at = datetime.now() + timedelta(hours=1)
        super().save(*args, **kwargs)
        
    
    