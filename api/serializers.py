# from typing_extensions import Required
from django.db.models import fields
from requests import models
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import FavouriteCharacters, FavouriteQuotes


# the serializer for Signup
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "password"]


# the serializer for Favorites Character
class FavouriteCharactersSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavouriteCharacters
        fields = ["_id", "height", "race", "gender", "birth",
                  "spouse", "death", "realm", "hair", "name", "wikiUrl", ]


# the serializer for Favorite Quotes
class FavouritesQuotesSerializer(serializers.ModelSerializer):

    class Meta:
        model = FavouriteQuotes
        fields = ["_id", "character", "dialog", "movie"]
