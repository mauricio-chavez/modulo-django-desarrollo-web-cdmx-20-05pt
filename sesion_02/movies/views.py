"""Movies app views"""

from django.shortcuts import render, get_object_or_404

from .models import Movie


def movies_list(response):
    """Lists all movies"""
    movies = Movie.objects.all().order_by('director__first_name')
    return render(response, 'list.html', {'movies': movies})


def movies_detail(response, pk):
    """Gets movie detail"""
    movie = get_object_or_404(Movie, pk=pk)
    return render(response, 'detail.html', {'movie': movie})
