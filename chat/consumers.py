import json

import simplejson
from channels.generic.websocket import WebsocketConsumer
from .models import Chat

connection_dict = dict()


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()



    def disconnect(self, close_code):
        pass

    # 如果code是250，代表是注册信息
    def receive(self, text_data):
        payload = simplejson.loads(text_data)

        if payload['code'] == "250":
            connection_dict[payload['id']] = self
        else:
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
            ret = simplejson.dumps({"from": sender, "to": receiver, "content": content, "chat_id": chat.chat_id, "chat_read": chat.read,
                       "create_time": int(chat.create_time.now().timestamp())})
            if receiver in connection_dict:
                connection_dict[receiver].send(ret)
            self.send(ret)
