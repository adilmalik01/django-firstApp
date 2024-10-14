from django import forms
from .models import Book
from django.contrib.auth.models import User



class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'password', 'email']



class ContactForm(forms.ModelForm):
       class Meta:
           model = Book
           fields = ['title','authoName','description','image']
           
       

