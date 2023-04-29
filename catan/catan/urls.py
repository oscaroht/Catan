"""catan URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from users import views as user_views
from game import views as game_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.RegisterView.as_view(), name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),  # overwrite template to users/login
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', user_views.ProfileView.as_view(), name='profile'),
    path('', game_views.home, name='game-home'),
    path('createnewgame', game_views.CreateNewGameView.as_view(), name='game-createnewgame'),
    path('mygames', game_views.MyGamesView.as_view(), name='mygames'),
    path('game/<int:pk>', game_views.GameView.as_view(), name='game')
]
