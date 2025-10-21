# views.py
from .models import Book
from django.shortcuts import render

def booklist(request):
    books = Book.objects.all()
    return render(request, 'booklist.html', {'books': books})
