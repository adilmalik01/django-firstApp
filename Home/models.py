from django.db import models
from django import forms
# Create your models here.
class Book(models.Model):
    authoName =  models.CharField(max_length=20)
    title =  models.TextField()
    description =  models.TextField()
    image = models.ImageField(upload_to='book_images/', null=True, blank=True)  # New field for image

    
    
    def __str__(self):
        return self.title + " " + self.authoName
    
    
    
class product(models.Model):
    productName =  models.CharField(max_length=20)
    productPrice =  models.TextField()
    
    
    def __str__(self):
        return self.productName
    

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['authoName', 'title', 'description']  # Include all fields you want to edit