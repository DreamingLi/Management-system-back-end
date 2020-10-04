from channels.routing import ProtocolTypeRouter,URLRouter
from django.conf.urls import url
import chat.routing

application = ProtocolTypeRouter({
    'websocket':URLRouter(
        chat.routing.websocket_urlpatterns
    )
})