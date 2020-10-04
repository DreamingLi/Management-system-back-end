import json

import simplejson
from channels.generic.websocket import WebsocketConsumer
from .models import Chat


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        payload = simplejson.loads(text_data)

        sender = payload['from']
        receiver = payload['to']
        content = payload['content']
        id = [sender, receiver]
        id.sort()
        chat = Chat()

        chat.sender = sender
        chat.receiver = receiver
        chat.content = content
        chat.chat_id = "_".join(id)
        chat.read = False
        chat.save()
        ret = {"from": sender, "to": receiver, "content": content, "chat_id": id, "chat_read": chat.read,
               "create_time": int(chat.create_time.now().timestamp())}
        self.send(simplejson.dumps(ret))
