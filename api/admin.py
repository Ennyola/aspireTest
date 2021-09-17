from django.contrib import admin
from .models import FavouriteCharacters, FavouriteQuotes
# Register your models here.

admin.site.register(FavouriteCharacters)
admin.site.register(FavouriteQuotes)
