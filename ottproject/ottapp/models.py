from django.db import models

class Customer(models.Model):
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    dob = models.DateField()
    phone_number = models.CharField(max_length=15, unique=True)

    def _str_(self):
        return self.username




# models.py in ottapp
from django.db import models

class Actor(models.Model):
    name = models.CharField(max_length=255)
    bio = models.TextField()

    def _str_(self):
        return self.name

class Director(models.Model):
    name = models.CharField(max_length=255)
    bio = models.TextField()

    def _str_(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def _str_(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    release_date = models.DateField()
    url = models.URLField()
    genres = models.ManyToManyField(Genre)
    poster = models.ImageField(upload_to='movie_posters/', null=True, blank=True)
    cast = models.ManyToManyField(Actor)
    language = models.CharField(max_length=50)
    age_rating = models.CharField(max_length=10)
    director = models.ForeignKey(Director, on_delete=models.SET_NULL, null=True, blank=True)

    def _str_(self):
        return self.title