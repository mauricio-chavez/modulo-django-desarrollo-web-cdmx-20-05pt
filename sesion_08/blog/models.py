"""Blog models"""

from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    """Post model"""
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Returns a post string representation"""
        return '{} | {}'.format(self.title, self.author.username)
