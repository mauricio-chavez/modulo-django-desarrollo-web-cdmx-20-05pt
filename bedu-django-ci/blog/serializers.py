"""Blog app serializers"""

from django.contrib.auth.models import User

from rest_framework import serializers

from .models import Post


class PostSerializer(serializers.ModelSerializer):
    """Post model serializer"""
    class Meta:
        model = Post
        fields = ['title', 'content']

    def create(self, validated_data):
        """Creates a new post"""
        user = User.objects.first()
        return Post.objects.create(author=user, **validated_data)
