"""Movies app URL Configuration"""

from django.urls import path

from .views import hello_world, suma

urlpatterns = [
    path('hello', hello_world),
    path('suma/<int:primero>/<int:segundo>', suma),
]
