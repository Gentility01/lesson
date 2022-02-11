from pyexpat import model
from unicodedata import name
from django import forms
from django.contrib.auth.forms import  UserCreationForm
from .models import User, Customer, Employee
from django.db import transaction
from django.contrib.auth import authenticate
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget
from django.core.exceptions import ValidationError 


class CustomerSignupForm(UserCreationForm):
    location = forms.CharField(required=True)
    country = CountryField(blank_label='Select your country').formfield()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({
            'required':'',
            'name':'first_name',
            'class':'form-control',
            'placeholder':'First name',
            'type':'text',
        })
        self.fields['last_name'].widget.attrs.update({
            'required':'',
            'name':'last_nannme',
            'class':'form-control',
            'placeholder':'Last name',
            'type':'text',
        })
        self.fields['username'].widget.attrs.update({
            'required':'',
            'name':'username',
            'class':'form-control',
            'placeholder':'Username',
            'type':'text',
        })
        self.fields['email'].widget.attrs.update({
            'required':'',
            'name':'username',
            'class':'form-control',
            'placeholder':'Email',
            'type':'email',
        })
        self.fields['password1'].widget.attrs.update({
            'required':'',
            'name':'password1',
            'class':'form-control',
            'placeholder':'Password',
            'type':'password',
        })
        self.fields['password2'].widget.attrs.update({
            'required':'',
            'name':'password2',
            'class':'form-control',
            'placeholder':'Retype password',
            'type':'password',
        })
        self.fields['location'].widget.attrs.update({
            'required':'',
            'name':'location',
            'class':'form-control',
            'placeholder':'Location',
            'type':'text',
        })
        self.fields['country'].widget.attrs.update({
            'required':'',
            'name':'country',
            'class':'form-control',
            'placeholder':'Location',
            'country':CountrySelectWidget()
        })
   
    
    
    class Meta(UserCreationForm.Meta):
        model = User
        fields =  ['first_name', 'last_name', 'username', 'email', 'password1', 'password2', 'location']
        
    def clean_password2(self):  
        password1 = self.cleaned_data['password1']  
        password2 = self.cleaned_data['password2']  
  
        if password1 and password2 and password1 != password2:  
            raise ValidationError("Password don't match")  
        return password2  
  
        
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_employee = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.email = self.cleaned_data.get('email')
        user.save()
        customer = Customer.objects.create(user=user)
        customer.location = self.cleaned_data.get('location')
        customer.country = self.cleaned_data.get('country')
        customer.save()
        return user
    
    
    
class EmployeeSignupForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    phone_number = forms.CharField(required=True)
    descignation = forms.CharField(required=True)
    
    
    
    class Meta(UserCreationForm.Meta):
        model = User
        fields =  ['first_name', 'last_name', 'username', 'password1', 'password2',  'phone_number']
        
        
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_employee = True
        user.is_customer = True
        user.is_staff = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.save()
        employee = Employee.objects.create(user=user)
        employee.phone_number=self.cleaned_data.get('phone_number')
        employee.descignation=self.cleaned_data.get('descignation')
        employee.save()
        return user
    
    
    


