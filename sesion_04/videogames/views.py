"""Videogames app"""

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import TemplateView


class WelcomeView(LoginRequiredMixin, TemplateView):
    """Shows welcome"""
    template_name = 'videogames/welcome.html'


@login_required
def welcome(request):
    return render(request, 'videogames/welcome.html')
