from django.shortcuts import render, redirect , get_object_or_404
from .models import Book , BookForm
from .form import ContactForm, UserRegistrationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

@login_required
def RenderHome(request):
    books = Book.objects.all()
    return render(request, "index.html", context={'books': books})

@login_required
def About(request):
    return render(request, "about.html")


@login_required
def Service(request):
    return render(request, "service.html")


@login_required
def Contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)  # Include request.FILES to handle image uploads
        if form.is_valid():
            form.save()  # Save the form along with the uploaded image
            return redirect('/')  # Redirect after successful save
    else:
        form = ContactForm()

    return render(request, "contact.html", {'form': form})


def signup(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():    
            user = form.save() 
            login(request, user)  
            return redirect('/') 
    else:
        form = UserRegistrationForm()
    return render(request, 'signup.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'profile.html')

def custom_logout_view(request):
    logout(request) 
    request.session.flush() 
    response = redirect('login')  
    response.delete_cookie('sessionid')  
    return response


@login_required
def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'book_detail.html', {'book': book})



@login_required
def book_update(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book) 
        if form.is_valid():
            form.save()
            return redirect('book_detail', book_id=book.id)
    else:
        form = BookForm(instance=book)

    return render(request, 'book_update.html', {'form': form, 'book': book})


@login_required
def book_delete(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    if request.method == 'POST':
        book.delete()
        return redirect('home')  # Redirect to home after deletion

    return render(request, 'book_delete.html', {'book': book})