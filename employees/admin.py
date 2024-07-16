from django.contrib import admin

# Register your models here.
from .models import Employee, PasswordResetToken

admin.site.register(Employee)
admin.site.register(PasswordResetToken)
