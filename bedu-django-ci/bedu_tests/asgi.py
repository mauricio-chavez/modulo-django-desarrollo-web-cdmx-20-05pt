"""
ASGI config for bedu_tests project.
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bedu_tests.settings')

application = get_asgi_application()
