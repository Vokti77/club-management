from django.urls import path
from django.core.asgi import get_asgi_application
from . import consumers

websocket_urlpatterns = [
    path('ws/<str:room_name>/', consumers.ChatConsumer.as_asgi()),
]