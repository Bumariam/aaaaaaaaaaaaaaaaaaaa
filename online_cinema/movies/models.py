from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Actor(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='photo', null=True, blank=True)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='photo', null=True, blank=True)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    actors = models.ManyToManyField(Actor)
    description = models.TextField()
    release_year = models.IntegerField()
    duration = models.IntegerField()
    rating = models.FloatField()

    def __str__(self):
        return self.title


class Photo(models.Model):
    name = models.CharField(max_length=100)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, null=True, blank=True)
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE, null=True, blank=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to='photo')

    def __str__(self):
        return self.name