from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/tabletop/<int:campaign_id>/', consumers.TabletopConsumer.as_asgi()),
]
