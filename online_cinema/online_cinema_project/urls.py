from django.contrib import admin
from django.urls import path
from movies.views import genre_movies, movie_details, genre_list, movie_list_by_genre

urlpatterns = [
    path('admin/', admin.site.urls),
    path('genre/<int:genre_id>/', genre_movies, name='genre_movies'),
    path('movie/<int:movie_id>/', movie_details, name='movie_details'),
    path('genres/', genre_list, name='genre_list'),
    path('genre/<int:genre_id>/movies/', movie_list_by_genre, name='movie_list_by_genre'),
]
