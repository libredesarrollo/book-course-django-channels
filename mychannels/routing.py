'''
Para habilitar la app en Vue se emplea la autenticacion mediante tokens y el MW
TokenAuthMiddleware, aparte de la app de alerta

Para habilitar la app de multiple canales en Django se emplea la autenticacion 
AuthMiddlewareStack y la app de chat

Debes de des/comentar las lineas segun la app que quieras habilitar
'''


from channels.routing import ProtocolTypeRouter, URLRouter

# from channels.auth import AuthMiddlewareStack
from alert.middlewares import TokenAuthMiddleware

# import chat.routing
import alert.routing

from django.core.asgi import get_asgi_application
django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter({
    "http": django_asgi_app,
    # 'websocket' : AuthMiddlewareStack(
    'websocket': TokenAuthMiddleware(
        # URLRouter(chat.routing.websocket_urlpatterns)
        URLRouter(alert.routing.websocket_urlpatterns)
    )
})
