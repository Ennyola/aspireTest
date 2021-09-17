from os import name
from django.urls import path, include
from .views import CharacterView, CharacterQuotesView, SaveFavoriteCharacter, Signup, Login, FavouriteCharactersView, SaveFavouritesQuotes

urlpatterns = [
    path('characters/', CharacterView.as_view(), name="characters"),
    path('characters/<slug:id>/quotes/',
         CharacterQuotesView.as_view(), name="quotes"),
    path('characters/<slug:id>/favorites/', SaveFavoriteCharacter.as_view()),
    path('characters/<slug:id1>/quotes/<slug:id2>/favorites/',
         SaveFavouritesQuotes.as_view()),
    path('favorites/', FavouriteCharactersView.as_view()),
    path('login/', Login.as_view(), name="login"),
    path('signup/', Signup.as_view(), name="signup"),


]
