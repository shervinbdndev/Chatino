from django.urls import path
from . import consumers


websocket_urlpatterns = [
    path(
        route='ws/<str:room_name>/',
        view=consumers.ChatRoomConsumer.as_asgi(),
    )
]