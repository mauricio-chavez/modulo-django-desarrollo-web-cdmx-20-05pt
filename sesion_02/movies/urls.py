"""Movies app URL config"""

from django.urls import path

from .views import movies_list, movies_detail

app_name = 'movies'

urlpatterns = [
    path('', movies_list, name='list'),
    path('detail/<int:pk>', movies_detail, name='detail'),
]
