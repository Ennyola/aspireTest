import requests
from django.conf import settings
from django.contrib.auth import login
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.serializers import AuthTokenSerializer
from .serializers import RegisterSerializer, FavouriteCharactersSerializer, FavouritesQuotesSerializer
from .models import FavouriteCharacters, FavouriteQuotes


# Create your views here.

# This returns a list of characters
class CharacterView(APIView):
    def get(self, request):
        characters = requests.get(
            "https://the-one-api.dev/v2/character", headers=settings.HEADERS).json()
        return Response(characters)


# This returns all the quotes for a single character
class CharacterQuotesView(APIView):
    def get(self, request, id):
        try:
            quote = requests.get(
                f"https://the-one-api.dev/v2/character/{id}/quote", headers=settings.HEADERS).json()
            return Response(quote, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

# This registers the user


class Signup(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            if User.objects.filter(email=email).exists():
                return Response("Email already exists", status=status.HTTP_400_BAD_REQUEST)
            serializer.save()
            user = User.objects.get(email=email)
            user.set_password(serializer.validated_data['password'])
            user.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# This view logs the user in and then returns a token to the user for subsequent authentications
class Login(APIView):
    def post(self, request):
        serializer = AuthTokenSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                'email': user.email,
                'username': user.username,
                'token': token.key,
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# This saves a users favourite character to the database
class SaveFavoriteCharacter(APIView):
    permission_classes = [IsAuthenticated]

    # This returns a single character so a user can add it to favorites characters Table
    def get(self, request, id):
        try:
            character = requests.get(
                f"https://the-one-api.dev/v2/character/{id}", headers=settings.HEADERS).json()
            print(character)
            return Response(character, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    # This saves the single character to the database
    def post(self, request, id):
        serializer = FavouriteCharactersSerializer(data=request.data)
        if serializer.is_valid():
            user = request.user
            character_id = serializer.validated_data["_id"]
            height = serializer.validated_data["height"]
            race = serializer.validated_data["race"]
            gender = serializer.validated_data["gender"]
            birth = serializer.validated_data["birth"]
            spouse = serializer.validated_data["spouse"]
            death = serializer.validated_data["death"]
            realm = serializer.validated_data["realm"]
            hair = serializer.validated_data["hair"]
            name = serializer.validated_data["name"]
            wikiUrl = serializer.validated_data["wikiUrl"]
            favourites = FavouriteCharacters(user=user, _id=character_id, height=height, race=race, gender=gender,
                                             birth=birth, spouse=spouse, realm=realm, hair=hair, name=name, wikiUrl=wikiUrl)
            favourites.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# This saves a user's favorite quote to the database


class SaveFavouritesQuotes(APIView):
    permission_classes = [IsAuthenticated]

    # This returns a single quote so a user can add it to favorites
    def get(self, request, id1, id2):
        try:
            quote = requests.get(
                f"https://the-one-api.dev/v2/quote/{id2}", headers=settings.HEADERS).json()
            return Response(quote, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    # This saves the single character to the database
    def post(self, request, id1, id2):
        serializer = FavouritesQuotesSerializer(data=request.data)
        if serializer.is_valid():
            user = request.user
            quotes_id = serializer.validated_data["_id"]
            dialog = serializer.validated_data["dialog"]
            movie = serializer.validated_data["movie"]
            character_id = serializer.validated_data["character"]
            favourite_quotes = FavouriteQuotes(
                character=character_id, _id=quotes_id, dialog=dialog, movie=movie)
            favourite_quotes.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# This view returns all the favorite characters for a single authenticated user
class FavouriteCharactersView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        favourites = FavouriteCharacters.objects.filter(user=request.user)
        serializers = FavouriteCharactersSerializer(favourites, many=True)
        return Response(serializers.data)
