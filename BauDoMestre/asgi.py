import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator
import chat.routing
import tabletop.routing


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'BauDoMestre.settings')

django_asgi_app = get_asgi_application()

# Defina o roteador de protocolos para aplicação ASGI
application = ProtocolTypeRouter({
    "http": django_asgi_app,  # Roteia conexões HTTP padrão para a aplicação Django
    "websocket": AllowedHostsOriginValidator(  # Roteia conexões WebSocket
        AuthMiddlewareStack(
            URLRouter(
                chat.routing.websocket_urlpatterns +  # Rotas WebSocket do chat
                tabletop.routing.websocket_urlpatterns  # Rotas WebSocket do tabletop
            )
        ),
    ),
})