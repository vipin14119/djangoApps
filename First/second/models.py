from __future__ import unicode_literals

from django.db import models


class Movie(models.Model):
    title=models.CharField(max_length=200)
    comment=models.CharField(max_length=200)
    rating=models.IntegerField(default=0)
    def __unicode__(self):
        return self.title

class Extended(models.Model):
    heading=models.ForeignKey(Movie)
    ratingtype=models.CharField(max_length=200)
    rate=models.IntegerField(default=0)
# Create your models here.
