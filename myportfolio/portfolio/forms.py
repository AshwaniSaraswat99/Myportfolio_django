from django import forms
from .models import contact
from django.contrib.auth.models import User #we have to import validation models for user 
from django.contrib.auth.forms import UserCreationForm

class contactform(forms.ModelForm):
    class Meta:
        model = contact
        fields = ['name', 'email', 'subj', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'}),
            'subj': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your Message'}),
        }

class registrationform(UserCreationForm):
    email=forms.EmailField(required=True, max_length=254, help_text='Add valid email such as abc@email.com')
    class Meta:
        model=User
        fields=['username','email','password1','password2']