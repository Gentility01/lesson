from django import forms
from django.db import models
from django.db.models import fields
from .models import Article


class ArticleModelForm(forms.ModelForm):
    
    title   = forms.CharField( max_length=150, widget=forms.TextInput(attrs={
        'placeholder':'Your title'
    }))
    
    content  = forms.CharField(max_length=160, required=False, widget=forms.Textarea(attrs={
        'class': 'new-class',
        'rows':15,
        'cols':100,
        'placeholder':'Your description'
    }))
    
  
    class  Meta :
        model  =  Article
        fields =[
           'title',
           'content',
           'active'
       ]