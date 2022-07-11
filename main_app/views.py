from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Book
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def book_index(request):
    books = Book.objects.all()
    return render(request, 'books/index.html', {'books': books})


class BookCreate(CreateView):
    model = Book
    fields = ['name', 'genre', 'description', 'author']
    success_url = '/books/'