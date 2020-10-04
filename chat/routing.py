from channels.routing import ProtocolTypeRouter, URLRouter
from django.conf.urls import url
from django.urls import path

from chat.consumers import ChatConsumer

websocket_urlpatterns = [
    path('chat', ChatConsumer),
    path('socket.io/', ChatConsumer)
]
