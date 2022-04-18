"""django_boilerplate URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import re_path, path, include
from django.contrib.auth import views as auth_views
from login_boilerplate import views


urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('login/', auth_views.LoginView.as_view()),
    path('logout/', auth_views.LogoutView.as_view()),
    re_path(r'^registration/$', views.registration, name='registration'),
    re_path(r'^account_activation_sent/$', views.account_activation_sent, name='account_activation_sent'),
    path(
        'activate/<uidb64>/<token>/',
        views.activate,
        name='activate'
    ),
    re_path(r'^home/$', views.home, name='home'),
]
