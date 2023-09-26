from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Library(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(editable=False)
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.date_created = timezone.now()
        
        return super().save(*args, **kwargs)