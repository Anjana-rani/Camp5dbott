from django.db import models

# models.py in ottapp
# models.py in ottapp
from django.db import models
from django.utils import timezone

# models.py in ottapp
from django.db import models
from django.utils import timezone


class Customer(models.Model):
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    dob = models.DateField()
    phone_number = models.CharField(max_length=15, unique=True)
    expiration_date = models.DateField(blank=True, null=True)

    def is_membership_expired(self):
        return self.expiration_date and self.expiration_date < timezone.now().date()

    def renew_membership(self, payment_method):
        if payment_method == 'basic':
            self.expiration_date = timezone.now().date() + timezone.timedelta(minutes=5)
        elif payment_method == 'standard':
            self.expiration_date = timezone.now().date() + timezone.timedelta(weeks=12)
        elif payment_method == 'premium':
            self.expiration_date = timezone.now().date() + timezone.timedelta(weeks=24)

        self.save()

    def __str__(self):
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