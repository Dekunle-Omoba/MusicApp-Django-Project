from tkinter import CASCADE
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.


class Artiste(models.Model):
    first_name = models.TextField
    last_name = models.CharField(_MAX_LENGTH-50)
    age = models.IntegerField(_MAX_LENGTH-10)


class Song(models.Model):
 song_title = models.CharField(_MAX_LENGTH-50)
 date_released = models.DateField(_MAX_LENGTH-25)
 likes = models.IntegerField(_MAX_LENGTH-25)
 Artiste_id = models.IntegerField(_MAX_LENGTH-25)


class Lyric(models.Model):
 content  = models.CharField(_MAX_LENGTH-300)
 song_id = models.IntegerField(_MAX_LENGTH-25)