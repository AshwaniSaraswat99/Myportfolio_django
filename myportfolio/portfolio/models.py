from django.db import models
from django.utils import timezone
# Create your models here.

class contact(models.Model):
    name=models.CharField(max_length=200)
    subj = models.CharField(max_length=200, default='')
    email=models.EmailField(max_length=200)
    message=models.TextField()
    created_at=models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.name

