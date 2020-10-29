"""Users app views"""

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import views as auth_views
from django.forms.forms import Form
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import FormView

from .forms import SignupForm

# Class based views


class LoginView(auth_views.LoginView):
    """Authenticates a user"""
    template_name = 'users/login.html'
    redirect_authenticated_user = True


class LogoutView(auth_views.LogoutView):
    """Logs out a user"""


class SignupView(FormView):
    """Creates and logs in a user"""
    template_name = 'users/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('videogames:welcome')

    def form_valid(self, form):
        """Saves and logs in a user"""
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)


# Function based views


def login_view(request):
    """Authenticates a user"""
    if request.user.is_authenticated:
        return redirect('videogames:welcome')

    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            return redirect('videogames:welcome')
        else:
            context['error'] = 'Las credenciales no coinciden.'

    return render(request, 'users/login.html', context)


def logout_view(request):
    """Logs out a user"""
    logout(request)
    return redirect('users:login')


def signup(request):
    """Creates users"""
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('videogames:welcome')
    return render(request, 'users/signup.html', {'form': form})
