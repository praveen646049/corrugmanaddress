"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
# address_software/urls.py
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views  # Ensure this line is included
from myapp.views import custom_login, welcome

urlpatterns = [
    path('', welcome, name='welcome'), 
    path('admin/', admin.site.urls),
    path('login/', custom_login, name='login'),  # Custom login view
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # Properly reference auth_views
    path('', include('myapp.urls')),  # Include your app URLs
]
