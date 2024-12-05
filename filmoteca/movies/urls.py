from django.urls import path
from .views import FilmView, FavoriteView

urlpatterns = [
    path('', FilmView.as_view(), name='film_list_add'),
    path('films/', FilmView.as_view(), name='create_film'),
    path('favorites/', FavoriteView.as_view(), name='favorite_list_create'),
    path('favorites/<int:pk>/', FavoriteView.as_view(), name='favorite_detail')
]
