import json

from django.utils import dateformat, timezone

from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        print('Conectado')

        self.id = self.scope['url_route']['kwargs']['room_id']
        self.room_group_name = 'chat_%s' % self.id
        self.user = self.scope['user']

        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

        await self.accept()
        # return super().connect()

    async def disconnect(self, code):
        print("Desconectado")
        await self.channel_layer.group_discard(self.room_group_name,self.channel_name)

        # return super().disconnect(code)

    async def receive(self, text_data):
        print("Recibido"+text_data)

        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'username': self.user.username,
                'datetime': dateformat.format(timezone.now(), 'Y-m-d H:i:s')
            }
        )

        print(message)

    async def chat_message(self, event):
        message = event['message']
        username = event['username']
        datetime = event['datetime']
        await self.send(text_data=json.dumps({ 'message':message, 'username':username, 'datetime':datetime }))

        # return super().receive(text_data, bytes_data)