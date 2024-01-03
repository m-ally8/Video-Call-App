from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import path
from .consumers import VideoCallConsumer

application = ProtocolTypeRouter(
    {
        'websocket': AuthMiddlewareStack(
            URLRouter(
                #Add Websocket URL routing here
                path('ws/video_call/', VideoCallConsumer.as_asgi()),
            )

        ),
    }
)