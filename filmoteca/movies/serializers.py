from rest_framework import serializers
from .models import Film, Favorite

class FilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = ['id', 'title', 'description', 'release_date']


class FavoriteSerializer(serializers.ModelSerializer):
    film = FilmSerializer(read_only=True)  # Полная информация о фильме
    film_id = serializers.PrimaryKeyRelatedField(queryset=Film.objects.all(), write_only=True, source='film')  # Только ID для создания

    class Meta:
        model = Favorite
        fields = ['id', 'user_id', 'film', 'film_id']
