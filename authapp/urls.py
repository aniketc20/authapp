"""authapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from django.contrib.auth import views as auth_views
from allauth.account import views
from simpleauth.views import (
    Login,
    Logout,
    Dashboard
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Login.as_view(), name='login'),
    path("password-reset", views.PasswordResetView.as_view(), name="password_reset"),
    path(r"^password/reset/key/(?P<uidb36>[0-9A-Za-z]+)-(?P<key>.+)/$", views.PasswordResetFromKeyView.as_view(template_name = 'account/password_reset_confirm.html'), name="password_set"),
    path('logout/', Logout.as_view(), name="logout"),
    path('dashboard/', Dashboard.as_view(), name="dashboard"),
    path('accounts/', include('allauth.urls')),
]
