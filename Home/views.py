from django.shortcuts import render , redirect
from .models import Book
from .form import ContactForm

def RenderHome(request):
    books = Book.objects.all()
    return render(request, "index.html", context={'books': books })

def About(request):
    return render(request , "about.html")


def Service(request):
    return render(request , "service.html")

def Contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            
            
        return  redirect('/') 
    else:
        form = ContactForm()
    return render(request , "contact.html",{'form': form})
           
    
    
    
    