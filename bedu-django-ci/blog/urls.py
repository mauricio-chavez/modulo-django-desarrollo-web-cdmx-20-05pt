"""Blog app URL config"""

from django.urls import path

from .views import hello, list_posts, create_post, CreatePostView

app_name = 'blog'

urlpatterns = [
    path('', list_posts, name='list'),
    path('create/', create_post, name='create'),
    path('hello/<str:name>/', hello, name='hello'),
    path('api/create/', CreatePostView.as_view(), name='api_create')
]
