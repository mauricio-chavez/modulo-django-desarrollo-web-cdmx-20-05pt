"""Movies app models"""

from django.db import models


class Director(models.Model):
    """Director model"""
    first_name = models.CharField('nombre(s)', max_length=100)
    last_name = models.CharField('apellido(s)', max_length=100)
    birthday = models.DateField('cumpleaños')

    def __str__(self):
        """Returns a director string representation"""
        return self.first_name + ' ' + self.last_name


class Movie(models.Model):
    """Movie model"""
    name = models.CharField('nombre(s)', max_length=100)
    release_date = models.DateField('fecha de lanzamiento')
    director = models.ForeignKey('Director', on_delete=models.CASCADE)

    def __str__(self):
        """Returns a movie string representation"""
        return self.name
