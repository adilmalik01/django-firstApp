from django.shortcuts import render
from .models import Book

def RenderHome(request):
    books = Book.objects.all()
    return render(request, "index.html", context={'books': books})

def About(request):
    return render(request , "about.html")


def Service(request):
    return render(request , "service.html")

def Contact(request):
    return render(request , "contact.html")