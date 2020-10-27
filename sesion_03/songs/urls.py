"""Songs app urls"""

from django.urls import path

from .views import list_songs, create_album


app_name = 'songs'

urlpatterns = [
    path('', list_songs, name='list'),
    path('create-album/', create_album, name='create_album'),
]
