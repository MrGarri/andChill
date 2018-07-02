from django.db import models


class Movie(models.Model):
    name = models.CharField(max_length=80)
    video = models.CharField(max_length=500)
    description = models.CharField(max_length=1000, blank=True)
    year = models.CharField(max_length=10, blank=True)
    director = models.CharField(max_length=100, blank=True)
    actors = models.CharField(max_length=1000, blank=True)
    picture = models.CharField(max_length=500, blank=True)
    rating = models.CharField(max_length=20, blank=True)
