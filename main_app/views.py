from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Book
from django.forms import ModelForm
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import LastReadForm

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

@login_required
def book_index(request):
    books = Book.objects.filter(user=request.user)
    return render(request, 'books/index.html', {'books': books})

@login_required
def book_read(request):
    books = Book.objects.filter(read="Yes", user=request.user)
    return render(request, 'books/read_index.html', {'books': books})

@login_required
def want_to_read(request):
    books = Book.objects.filter(read='Want to read', user=request.user)
    return render(request, 'books/want_to_read_index.html', {'books': books})

@login_required
def book_detail(request, book_id):
    book = Book.objects.get(id=book_id)
    lastread_form = LastReadForm()
    return render(request, 'books/detail.html', {'book': book, 'lastread_form': lastread_form})



def add_reading(request, book_id):
  # create the ModelForm using the data in request.POST
  form = LastReadForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
    new_reading = form.save(commit=False)
    new_reading.book_id = book_id
    new_reading.save()
  return redirect('detail', book_id=book_id)


class BookCreate(LoginRequiredMixin, CreateView):
    model = Book
    fields = ['name', 'genre', 'author', 'publish_date','description', 'read']    
    success_url = '/books/'
      # This inherited method is called when a
  # valid cat form is being submitted
    def form_valid(self, form):
    # Assign the logged in user (self.request.user)
        form.instance.user = self.request.user  # form.instance is the cat
    # Let the CreateView do its job as usual
        return super().form_valid(form)

class BookDelete(LoginRequiredMixin, DeleteView):
    model = Book
    success_url = '/books/'

class BookUpdate(LoginRequiredMixin, UpdateView, ModelForm):
    model = Book
    fields = ['name', 'genre', 'author', 'read', 'description']

