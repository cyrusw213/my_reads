from django.db import models
from datetime import date
from django.contrib.auth.models import User
# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    def __str__(self):
        return self.name