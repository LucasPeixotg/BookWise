from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from book.models import Book

class Library(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    books = models.ManyToManyField(Book)
 
    date_created = models.DateTimeField(editable=False)
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(self).save(*args, **kwargs)
