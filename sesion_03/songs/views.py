"""Songs app views"""

from django.shortcuts import render, redirect

from .models import Song, Album


def list_songs(request):
    """Lists all songs"""
    songs = Song.objects.all()
    return render(request, 'list.html', {'songs': songs})


def create_album(request):
    """Create a album"""
    if request.method == 'POST':
        name = request.POST.get('name')
        cover = request.FILES.get('cover')
        Album.objects.create(name=name, cover=cover)
        return redirect('songs:list')
    else:
        return render(request, 'create.html')
