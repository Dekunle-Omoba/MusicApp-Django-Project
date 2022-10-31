
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.


class Artiste(models.Model):
    first_name = models.TextField
    last_name = models.TextField
    age = models.IntegerField(_MAX_LENGTH - 10)


class Song(models.Model):
    Artiste = models.ForeignKey(Artiste,on_delete=models.CASCADE)
    song_title = models.TextField
    date_released = models.DateField(_MAX_LENGTH - 25)
    likes = models.IntegerField(_MAX_LENGTH - 25)
    artiste_id = models.IntegerField(_MAX_LENGTH - 25)


class Lyric(models.Model):
    Song = models.ForeignKey(Song,on_delete=models.CASCADE)
    content = models.TextField
    song_id = models.IntegerField(_MAX_LENGTH - 10)
