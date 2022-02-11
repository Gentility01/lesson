from django.urls import path
from .views import register,customer_login,customer_register #CustomerUser, EmployeeUser


urlpatterns = [
    path('register/',register, name='register' ),
    path('custom_register/',customer_register, name='custom_register' ),
    # path('employee_register/',EmployeeUser.as_view(), name='employee_register' ),
    path('customer_login/',customer_login, name='customer_login' ),
]
