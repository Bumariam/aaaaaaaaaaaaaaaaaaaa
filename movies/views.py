from django.shortcuts import render, get_object_or_404
from .models import Genre, Movie

def genre_movies(request, genre_id):
    genre = Genre.objects.get(pk=genre_id)
    movies = Movie.objects.filter(genre=genre)
    return render(request, 'movies/genre_movies.html', {'genre': genre, 'movies': movies})

def movie_details(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    return render(request, 'movies/movie_details.html', {'movie': movie})




def genre_list(request):
    genres = Genre.objects.all()
    return render(request, 'genre_list.html', {'genres': genres})

def movie_list_by_genre(request, genre_id):
    genre = get_object_or_404(Genre, pk=genre_id)
    movies = Movie.objects.filter(genre=genre)
    return render(request, 'movie_list.html', {'genre': genre, 'movies': movies})
