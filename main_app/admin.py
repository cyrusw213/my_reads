from django.contrib import admin
from .models import Book, LastRead
# Register your models here.
admin.site.register(Book)
admin.site.register(LastRead)