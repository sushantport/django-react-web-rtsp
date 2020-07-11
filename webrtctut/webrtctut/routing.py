from channels.routing import ProtocolTypeRouter,URLRouter

from channels.auth import AuthMiddlewareStack

from django.urls import path
from rtspstream import consumer


websocket_urlPattern=[
    path('ws/rtsp/',consumer.Testserver),
]

application = ProtocolTypeRouter({
    # (http->django views is added by default)
    'websocket':AuthMiddlewareStack(URLRouter(websocket_urlPattern))
})