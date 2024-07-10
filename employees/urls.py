from django.urls import path
from .views import register_employee,register_employee,delete_employee,login,get_employee

urlpatterns = [
    path('register/', register_employee, name='register'),
    path('login/',login,name='login'),
    path('show/',get_employee,name='show_employees'),

    path('delete/<int:Empuc>/', delete_employee, name='delete'),

]
