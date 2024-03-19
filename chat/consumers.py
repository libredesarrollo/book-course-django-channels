import json
from channels.generic.websocket import WebsocketConsumer

class ChatConsumer(WebsocketConsumer):

    def connect(self):
        print('Conectado')
        self.accept()
        # return super().connect()

    def disconnect(self, code):
        print("Desconectado")
        # return super().disconnect(code)

    def receive(self, text_data):
        print("Recibido"+text_data)

        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        print(message)

        self.send(text_data=json.dumps({ 'message':message }))

        # return super().receive(text_data, bytes_data)