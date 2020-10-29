"""bedu_auth URL Configuration"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include(('users.urls', 'users'), namespace='users')),
    path('', include(('videogames.urls', 'videogames'), namespace='videogames')),
]
