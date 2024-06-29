from channels.generic.websocket import AsyncWebsocketConsumer
from channels.exceptions import StopConsumer
import json


class RadioConsumer(AsyncWebsocketConsumer):

    async def connect(self):

        await self.accept()

    async def receive(self, text_data=None, bytes_data=None):
        await self.send(text_data=text_data)

    async def disconnect(self, code):
        await self.close()

