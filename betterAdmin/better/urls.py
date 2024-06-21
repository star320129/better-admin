"""
URL configuration for better project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from django.views.static import serve
from django.conf import settings


urlpatterns = [

    path('api/v1/user/', include('src.Users.urls')),   # Users
    path('api/v1/perm/', include('src.Perms.urls')),   # rbac system

    path('media/<path:path>', serve, {'document_root': settings.MEDIA_ROOT}),   # media directory
]
