"""Movies app views"""

from django.http import HttpResponse
from django.shortcuts import render

from .models import Movie


def hello_world(request):
    """Lists movies"""
    if request.method == 'POST':
        name = request.POST['name']
        director = request.POST['director']
        Movie.objects.create(name=name, director=director)

    movies = Movie.objects.all()

    context = {
        'movies': movies
    }
    return render(request, 'hello.html', context)


def suma(request, primero, segundo):
    """Sums two numbers"""
    # nombre = request.GET['nombre'] # ?llave=valor&llave=valor
    resultado = primero + segundo
    return HttpResponse('El resultado es: ' + str(resultado))
