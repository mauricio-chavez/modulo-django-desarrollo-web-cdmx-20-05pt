"""Blog app views"""

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Post
from .serializers import PostSerializer


class CreatePostView(APIView):
    """Creates a post"""

    def post(self, request):
        """Creates post with POST"""
        serializer = PostSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)


def hello(request, name: str) -> HttpResponse:
    """Greets a user"""
    return HttpResponse('Hello, {}!'.format(name))


def list_posts(request):
    """Shows all posts"""
    posts = Post.objects.all()
    return render(request, 'blog/list.html', {'posts': posts})


@login_required
def create_post(request):
    """Shows all posts"""
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        Post.objects.create(title=title, content=content, author=request.user)
        return redirect('blog:list')

    return render(request, 'blog/create.html')
