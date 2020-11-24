"""Tests views for blog app"""

from django.test import TestCase, Client, RequestFactory
from django.contrib.auth.models import User

from ..views import hello
from ..models import Post


class BlogViewsTestCase(TestCase):
    """Tests my app"""

    def setUp(self):
        self.client = Client()
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='test',
            email='test@test.io',
            password='testing'
        )

    def test_hello_view(self):
        """Checks if hello view greets my user"""
        response = self.client.get('/hello/Mauricio/')
        self.assertContains(response, 'Hello, Mauricio!')

    def test_hello_view_with_factory(self):
        """Checks if hello view greets my user"""
        request = self.factory.get('/hello/Mauricio/')
        response = hello(request, 'Alberto')
        self.assertContains(response, 'Hello, Alberto!')

    def test_that_list_shows_my_post(self):
        """Tests that post appears in my app"""
        title = 'Post de prueba'
        content = 'Contenido de prueba'
        username = '@{}'.format(self.user.username)

        response = self.client.get('/')
        self.assertNotContains(response, title)
        self.assertNotContains(response, content)
        self.assertNotContains(response, username)

        Post.objects.create(title=title, content=content, author=self.user)

        response = self.client.get('/')
        self.assertContains(response, title)
        self.assertContains(response, content)
        self.assertContains(response, username)

    def test_that_create_with_post_actually_creates_a_post(self):
        """Tests that post is created"""
        title = 'Post de prueba creado'
        content = 'Contenido de prueba creado'

        self.client.login(username=self.user.username, password='testing')

        post_exists = Post.objects.filter(title=title).exists()
        self.assertFalse(post_exists)

        self.client.post('/create/', {'title': title, 'content': content})
        post_exists = Post.objects.filter(title=title).exists()
        self.assertTrue(post_exists)
