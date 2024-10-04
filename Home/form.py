from django import forms
from .models import Book

class ContactForm(forms.ModelForm):
       class Meta:
           model = Book
           fields = ['title','authoName','description']
           
       

