from django.urls import path
from employees.views import register_employee,delete_employee,login_emp,get_employee,update_employee,password_reset,password_reset_confirm

urlpatterns = [
    path('register/', register_employee, name='register'),
    path('login/',login_emp,name='login'),
    path('show/',get_employee,name='show_employees'),
    path('update/',update_employee,name='update_employee'),
    path('delete/<int:Empuc>/', delete_employee, name='delete'),
    path('password_reset/', password_reset, name='password_reset'),
    path('password_reset_confirm/<str:token>/',password_reset_confirm,name='password_reset_confirm')
]
