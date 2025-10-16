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

class Project(models.Model):
    P_id=models.CharField(max_length=20)
    title=models.CharField(max_length=200)
    description=models.TextField()
    image=models.ImageField(upload_to='portfolio/images/',blank=True, null=True)
    url=models.URLField(blank=True, null=True)
    created_at=models.DateTimeField(default=timezone.now,blank=True)
    Porject_made_on=models.DateField(blank=True, null=True)

    def __str__(self):
        return self.title
