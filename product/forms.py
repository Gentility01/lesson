from django import forms
from django.db import models
from django.forms import fields
from .models import Product



class ProductForm(forms.ModelForm):
    title   = forms.CharField( max_length=150, widget=forms.TextInput(attrs={
        'placeholder':'Your title'
    }))
    
    description  = forms.CharField(max_length=160, required=False, widget=forms.Textarea(attrs={
        'class': 'new-class',
        'rows':15,
        'cols':100,
        'placeholder':'Your description'
    }))
    
    email = forms.EmailField()   
    price = forms.DecimalField(initial=199.99 )
    
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price',
            'email'
            
        ]
        # authenticating the form from the forms.py
        # title is the name of the stuff you want to clean
    def clean_title(self, *args, **kwargs):
        title  = self.cleaned_data.get('title') 
        if not 'cfe' in title:
             raise forms.ValidationError('this is not a valid title need to add cfe ')
        if not 'news' in title:
            raise forms.ValidationError('this is not a valid title need to add news ')
        else:
           return title
       
    def clean_email(self, *args, **kwargs):
        email  = self.cleaned_data.get('email') 
        if not 'gmail.com' in email:
            raise forms.ValidationError('this is not a valid gmail account ')
        
        
        
        
class RawProductForm(forms.Form):
    title   = forms.CharField( max_length=150, widget=forms.TextInput(attrs={
        'placeholder':'Your title'
    }))
    description  = forms.CharField(max_length=160, required=False, widget=forms.Textarea(attrs={
        'class': 'new-class',
        'rows':15,
        'cols':100,
        'placeholder':'Your description'
    }))
    price = forms.DecimalField(initial=199.99 )
    
 
 
 