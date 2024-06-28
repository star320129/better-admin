from channels.generic.websocket import AsyncWebsocketConsumer
from channels.exceptions import StopConsumer


class SSHConsumer(AsyncWebsocketConsumer):

    async def websocket_connect(self, message):
        await self.accept()
        await self.channel_layer.group_add()
