"""Movies app model"""

from django.db import models


class Movie(models.Model):
    """Movie model"""
    name = models.CharField(max_length=255)
    director = models.CharField(max_length=255)

    def __str__(self):
        """Movie string representation"""
        return '{name} por {director}'.format(name=self.name, director=self.director)
