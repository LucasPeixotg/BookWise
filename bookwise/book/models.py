from django.db import models
from django.utils import timezone
from library.models import Library

class Book(models.Model):
    title = models.CharField(max_length=140)
    isbn = models.CharField(max_length=13)
    release_date = models.DateField(auto_now=False)
    modified_date = models.DateField(auto_now_add=True)
    authors = models.CharField(max_length=200)
    library_fk = models.ForeignKey(Library, on_delete=models.CASCADE)
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(self).save(*args, **kwargs)
