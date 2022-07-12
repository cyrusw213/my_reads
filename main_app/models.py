from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

HAVE_READ = (
        ('Yes', 'Yes'),
        ('Want to read', 'Want to read')
    )
class Book(models.Model):
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    publish_date = models.DateField()
    read = models.CharField(choices=HAVE_READ, max_length=15, default = HAVE_READ[0][0])
    class Meta:
        ordering = ['name']


    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('detail', kwargs={'book_id': self.id})
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class LastRead(models.Model):
        date = models.DateField()
        num_stars = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(10),
            MinValueValidator(1)
        ]
    )
        book = models.ForeignKey(Book, on_delete=models.CASCADE)
        def __str__(self):
            return f"{self.num_stars} on {self.date}"