import json

from django.utils import dateformat, timezone

from channels.generic.websocket import WebsocketConsumer

from asgiref.sync import async_to_sync

class ChatConsumer(WebsocketConsumer):

    def connect(self):
        print('Conectado')

        self.id = self.scope['url_route']['kwargs']['room_id']
        self.room_group_name = 'chat_%s' % self.id
        self.user = self.scope['user']

        async_to_sync(self.channel_layer.group_add)(self.room_group_name, self.channel_name)

        self.accept()
        # return super().connect()

    def disconnect(self, code):
        print("Desconectado")
        async_to_sync(self.channel_layer.group_discard)(self.room_group_name,self.channel_name)

        # return super().disconnect(code)

    def receive(self, text_data):
        print("Recibido"+text_data)

        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'username': self.user.username,
                'datetime': dateformat.format(timezone.now(), 'Y-m-d H:i:s')
            }
        )

        print(message)

    def chat_message(self, event):
        message = event['message']
        username = event['username']
        datetime = event['datetime']
        self.send(text_data=json.dumps({ 'message':message, 'username':username, 'datetime':datetime }))

        # return super().receive(text_data, bytes_data)