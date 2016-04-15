from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

class Users(models.Model):
    name=models.CharField(max_length=200)
    rollno=models.IntegerField(default=0)
    date=models.DateTimeField('date published')
    def __str__(self):
        return self.name
        
    

# Create your models here.
