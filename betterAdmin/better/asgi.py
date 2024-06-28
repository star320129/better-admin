"""
ASGI config for better project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from src.Wechat import routings


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'better.settings')

application = ProtocolTypeRouter({
    # websocket请求
    'websocket': URLRouter(routings.socket_urlpatterns),

    # http请求
    'http': get_asgi_application(),
})
