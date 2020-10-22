"""WSGI config for bedu_movies project."""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bedu_movies.settings')

application = get_wsgi_application()
