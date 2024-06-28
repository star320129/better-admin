from django.urls import path
from . import consumers

# 这个变量是存放websocket的路由
socket_urlpatterns = [
    # path('socket/<str:group>/', consumers),
]
