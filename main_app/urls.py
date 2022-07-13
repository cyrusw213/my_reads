from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('books/', views.book_index, name='index'),
    path('books/read', views.book_read, name='book_read' ),
    path('books/want_to_read', views.want_to_read, name='want_to_read' ),
    path('books/create', views.BookCreate.as_view(), name='books_create'),
    path('books/<int:book_id>', views.book_detail, name='detail'),
    path('books/<int:pk>/delete/', views.BookDelete.as_view(), name='books_delete'),
    path('books/<int:pk>/update/', views.BookUpdate.as_view(), name='books_update'),
    path('accounts/signup/', views.signup, name='signup'),
    path('books/<int:book_id>/add_reading', views.add_reading, name='add_reading')
]