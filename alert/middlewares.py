from rest_framework.authtoken.models import Token
from channels.db import database_sync_to_async


@database_sync_to_async
def get_user(token_key):
    try:
        token = Token.objects.get(key=token_key)
        return token.user
    except Token.DoesNotExist:
        return None

class TokenAuthMiddleware:

    def __init__(self, app):
        self.app = app

    async def __call__(self, scope, receive, send):

        token = scope['query_string'].decode('utf-8')
        if len(token.split('_')) == 2:
            token_name, token_key = token.split('_')
            if token_name=='Token':
                scope['user'] = await get_user(token_key)

        return await self.app(scope, receive, send)