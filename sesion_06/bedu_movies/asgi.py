"""ASGI config for bedu_movies project."""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bedu_movies.settings')

application = get_asgi_application()
