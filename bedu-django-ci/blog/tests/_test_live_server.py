"""Test suite with Live Server"""

from django.contrib.auth.models import User
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.test import Client
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from ..models import Post


# from django.test import LiveServerTestCase


class SeleniumBlogTests(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver()
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def setUp(self):
        """Authenticates user"""
        client = Client()
        username = 'tests'
        password = 'password_test'
        User.objects.create_user(
            username=username,
            password=password,
            email='me@test.io'
        )
        client.login(username=username, password=password)

        cookie = client.cookies['sessionid']

        self.selenium.get(self.live_server_url + '/admin/')
        self.selenium.add_cookie({
            'name': 'sessionid',
            'value': cookie.value,
            'secure': False,
            'path': '/'
        })
        self.selenium.refresh()
        self.selenium.get(self.live_server_url + '/admin/')

    def test_create_user(self):
        posts_count = Post.objects.count()
        self.assertEqual(posts_count, 0)

        title = 'Mi nuevo post'
        content = 'Mi contenido en mi post'

        self.selenium.get('{}/{}'.format(self.live_server_url, 'create/'))

        title_input = self.selenium.find_element(By.ID, "title-id")
        title_input.send_keys(title)

        content_input = self.selenium.find_element(By.ID, "content-id")
        content_input.send_keys(content)

        self.selenium.find_element(By.TAG_NAME, 'button').click()

        posts_count = Post.objects.count()
        self.assertEqual(posts_count, 1)

        post = Post.objects.first()
        self.assertEqual(post.title, title)
        self.assertEqual(post.content, content)
