"""Songs app models"""

from django.db import models


class TimestampModel(models.Model):
    """Model for inherit"""
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Song(TimestampModel):
    """Song model"""
    name = models.CharField(max_length=100)
    artist = models.ForeignKey(to='Artist', on_delete=models.CASCADE)
    album = models.ForeignKey(to='Album', on_delete=models.CASCADE)

    def __str__(self):
        """Returns song string representation"""
        return self.name


class Artist(TimestampModel):
    """Artist model"""
    name = models.CharField(max_length=100)

    def __str__(self):
        """Returns artist string representation"""
        return self.name


class Album(TimestampModel):
    """Album model"""
    name = models.CharField(max_length=100)
    cover = models.ImageField(upload_to='covers')

    def __str__(self):
        """Returns album string representation"""
        return self.name
