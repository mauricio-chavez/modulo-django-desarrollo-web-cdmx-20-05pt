"""Movies app models"""

from django.db import models


class Movie(models.Model):
    """Movie model"""
    name = models.CharField(max_length=75, unique=True)
    director = models.ForeignKey(to='Director', on_delete=models.CASCADE)
    sinopsis = models.TextField()
    release_date = models.DateField()

    def __str__(self):
        """Movie string representation"""
        return self.name


class Director(models.Model):
    """Director model"""
    first_name = models.CharField(max_length=75)
    last_name = models.CharField(max_length=75)
    birthday = models.DateField()

    def __str__(self):
        """Movie string representation"""
        return self.first_name + ' ' + self.last_name
