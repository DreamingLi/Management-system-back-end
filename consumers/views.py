from django.shortcuts import render

# Create your views here.
from channels.generic.websocket import WebsocketConsumer

consumer_object_list = []


class ChatConsumer(WebsocketConsumer):
    def websocket_connect(self, message):
        self.accept()
        consumer_object_list.append(self)
        pass

    def websocket_receive(self, message):
        print(self,message)
        pass

    def websocket_disconnect(self, message):
        pass
