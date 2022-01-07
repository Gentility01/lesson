from django import forms
from django.db.models import fields
from .models import Courses

class CourseModelForm(forms.ModelForm):
    title   = forms.CharField( max_length=150, widget=forms.TextInput(attrs={
        'placeholder':'Your title'
    }))
    class Meta:
        model = Courses
        fields = [
            'title'
        ]
        
    
    def clean_title(self):
        title = self.cleaned_data.get('title')
        if  'abc' not in title:
            raise forms.ValidationError('this is not a valid title')
        return title