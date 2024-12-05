from .serializers import FilmSerializer
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Favorite, Film
from .serializers import FavoriteSerializer


class FilmView(APIView):
    permission_classes = [AllowAny]
    """
     Просмотра списка фильмов.
    """
    def get(self, request, pk=None):
        """
        Retrieves details of a specific film if `pk` is provided,
        otherwise returns a list of all films.
        """
        if pk:  # Retrieve a specific film by ID
            try:
                film = Film.objects.get(pk=pk)
                serializer = FilmSerializer(film)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Film.DoesNotExist:
                return Response({'error': 'Film not found'}, status=status.HTTP_404_NOT_FOUND)
        else:  # Retrieve all films
            films = Film.objects.all()
            serializer = FilmSerializer(films, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """Добавление фильма"""
        serializer = FilmSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        """Изменение данных о фильме"""
        try:
            film = Film.objects.get(pk=pk)
        except Film.DoesNotExist:
            return Response({'error': 'Film not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = FilmSerializer(film, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """
        Удаляет фильм с указанным ID (pk).
        """
        try:
            film = Film.objects.get(pk=pk)
            film.delete()
            return Response({'message': 'Film deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        except Film.DoesNotExist:
            return Response({'error': 'Film not found'}, status=status.HTTP_404_NOT_FOUND)



class FavoriteView(APIView):
    """
    Handles adding, listing, retrieving, and deleting favorite films.
    """

    def get(self, request, pk=None):
        """
        Retrieves details of a specific favorite if `pk` is provided,
        otherwise lists all favorites for a given `user_id`.
        """
        if pk:  # Retrieve a specific favorite by ID
            try:
                favorite = Favorite.objects.get(pk=pk)
                serializer = FavoriteSerializer(favorite)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Favorite.DoesNotExist:
                return Response({'error': 'Favorite not found'}, status=status.HTTP_404_NOT_FOUND)
        else:  # List all favorites for a given user_id
            user_id = request.query_params.get('user_id')
            if not user_id:
                return Response({'error': 'user_id is required'}, status=status.HTTP_400_BAD_REQUEST)

            favorites = Favorite.objects.filter(user_id=user_id)
            serializer = FavoriteSerializer(favorites, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """
        Adds a film to the user's favorites.
        """
        serializer = FavoriteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        """
        Removes a specific favorite by `pk`.
        """
        if pk:  # Delete by ID
            try:
                favorite = Favorite.objects.get(pk=pk)
                favorite.delete()
                return Response({'message': 'Favorite deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
            except Favorite.DoesNotExist:
                return Response({'error': 'Favorite not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'error': 'pk is required for deletion'}, status=status.HTTP_400_BAD_REQUEST)