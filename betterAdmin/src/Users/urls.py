from django.contrib import admin
from django.urls import path
from . import views
from rest_framework.routers import SimpleRouter
router = SimpleRouter()
router.register('anyUser', views.LoginView, 'anyUser')
router.register('auth', views.UserView, 'auth')

urlpatterns = [

    path('admin/', admin.site.urls),

] + router.urls
