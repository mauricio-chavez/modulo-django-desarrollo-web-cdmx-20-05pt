"""Users app URL config"""

from django.urls import path

from . import views


urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    # path('login/', views.login_view, name='login'), # FBV
    path('logout/', views.LogoutView.as_view(), name='logout'),
    # path('logout/', views.logout_view, name='logout'), # FBV
    path('signup/', views.SignupView.as_view(), name='signup'),
    # path('signup/', views.signup, name='signup'), # FBV
]
