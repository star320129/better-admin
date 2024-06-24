from django.contrib import admin
from django.urls import path
from . import views
from rest_framework.routers import SimpleRouter
router = SimpleRouter()
router.register('anyUser', views.LoginView, 'anyUser')
router.register('action', views.UserView, 'action')
router.register('post', views.PostView, 'post')
router.register('online', views.OnlineUserView, 'online')

urlpatterns = [
    path('admin/', admin.site.urls),
] + router.urls
