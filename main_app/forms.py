from django.forms import ModelForm
from .models import Book

class MyBookForm(ModelForm):
  class Meta:
    model = Book
    fields = ['name', 'genre', 'description', 'author', 'num_stars', 'read']