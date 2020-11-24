"""Tests blog api"""

from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APITestCase

from ..models import Post


class BlogApiTests(APITestCase):
    """Tests API"""

    def setUp(self):
        """Create user"""
        self.user = User.objects.create_user(
            username='test',
            email='test@test.io',
            password='testing'
        )

    def test_create_post(self):
        title = 'Mi nuevo post en mi API'
        content = 'Mi contenido'

        post_count = Post.objects.count()
        self.assertEqual(post_count, 0)

        url = reverse('blog:api_create')
        payload = {'title': title, 'content': content}
        response = self.client.post(url, payload)
        self.assertEqual(response.data, payload)

        post_count = Post.objects.count()
        self.assertEqual(post_count, 1)

        post = Post.objects.first()
        self.assertEqual(post.title, title)
        self.assertEqual(post.content, content)
        self.assertEqual(post.author.id, self.user.id)
