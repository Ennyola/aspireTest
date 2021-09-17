from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class FavouriteCharacters(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default="")
    _id = models.CharField(max_length=500, default="", unique=True)
    height = models.CharField(max_length=500, default="", blank=True)
    race = models.CharField(max_length=500, default="", blank=True)
    gender = models.CharField(max_length=500, default="", blank=True)
    birth = models.CharField(max_length=500, default="", blank=True)
    spouse = models.CharField(max_length=500, default="", blank=True)
    death = models.CharField(max_length=500, default="", blank=True)
    realm = models.CharField(max_length=500, default="", blank=True)
    hair = models.CharField(max_length=500, default="", blank=True)
    name = models.CharField(max_length=500, default="", blank=True)
    wikiUrl = models.CharField(max_length=500, default="", blank=True)

    def __str__(self):
        return self.name


class FavouriteQuotes(models.Model):
    character = models.CharField(max_length=500, default="")
    _id = models.CharField(max_length=500, default="", unique=True)
    dialog = models.CharField(max_length=500, default="")
    movie = models.CharField(max_length=500, default="")

    def __str__(self):
        return self._id
