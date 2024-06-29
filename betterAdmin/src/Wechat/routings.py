from django.urls import re_path
from . import consumers

# 这个变量是存放websocket的路由
socket_urlpatterns = [
    re_path('socket/<pk:group>/', consumers.RadioConsumer.as_asgi()),
]
