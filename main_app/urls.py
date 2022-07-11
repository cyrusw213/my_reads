from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('books/', views.book_index, name='index'),
    path('books/create', views.BookCreate.as_view(), name='books_create')
]