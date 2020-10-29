"""Videogames app URL config"""

from django.urls import path

from . import views

urlpatterns = [
    path('', views.WelcomeView.as_view(), name='welcome'),
    # path('', views.welcome, name='welcome'), # FBV
]
