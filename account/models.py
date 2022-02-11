from django.db import models
from django.contrib.auth.models import AbstractUser
from django_countries.fields import CountryField


from django.db import models

# Create your models here.
class User(AbstractUser):
    is_customer  = models.BooleanField(default=False)
    is_employee  = models.BooleanField(default=False)
    first_name = models.CharField( max_length=100)
    last_name = models.CharField( max_length=100)
    
    
    
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    phone = models.CharField( max_length=100)
    location  = models.CharField( max_length=100)
    country = CountryField()
    
    
    
class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    phone = models.CharField( max_length=100)
    descignation  = models.CharField( max_length=100)
