

from pyexpat import model
from django.contrib import messages
import re
from types import new_class
from django.http import request
from django.shortcuts import render , redirect
from django.template import context
from .form import CustomerSignupForm, EmployeeSignupForm
from .models import User
from django.views.generic import CreateView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
# Create your views here.
def register(request):
    return render(request, 'account/register.html')



# class CustomerUser(CreateView):
#     model = User
#     form_class = CustomerSignupForm
#     template_name = 'account/customer_register.html'
    
#     def validation(self, form):
#         user=form.save()
#         login(self.request, user)
#         return redirect("/customer_login/")


def customer_register(request):
    form = CustomerSignupForm()
    if request.method == 'POST':
        form = CustomerSignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password1")
            form.save()
            new_user = authenticate(username=username, email=email, password=password)
            if new_user is not None:
                login(request, new_user)
                return redirect("homeview")

    else:
        form = CustomerSignupForm()
        
    context = {
            'form':form
        }
    return render(request, 'account/customer_register.html', context )
    
    

class EmployeeUser(CreateView):
    model = User
    form_class = EmployeeSignupForm
    template_name = 'account/employee_register.html'
    
    
def customer_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(usernme=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.error(request, 'Inalid Username or password')
        else:
            messages.error(request, 'Inalid Username or password')
    context={
        'form':AuthenticationForm()
    }
    return render(request, 'account/customer_login.html', context)
    
    
    


