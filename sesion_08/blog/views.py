"""Blog app views"""

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Post


def hello(request, name):
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
