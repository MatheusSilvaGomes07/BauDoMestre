from channels.db import database_sync_to_async
from .models import Token
import json
from channels.generic.websocket import AsyncWebsocketConsumer

class TabletopConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.campaign_id = self.scope['url_route']['kwargs']['campaign_id']
        self.campaign_group_name = f'campaign_{self.campaign_id}'

        await self.channel_layer.group_add(
            self.campaign_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.campaign_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        action = data.get('action')

        if action == 'load_map':
            map_id = data.get('map_id')
            await self.channel_layer.group_send(
                self.campaign_group_name,
                {
                    'type': 'load_map',
                    'map_id': map_id
                }
            )
        elif action == 'move_token':
            token_id = data.get('token_id')
            position_x = data.get('position_x')
            position_y = data.get('position_y')
            await self.channel_layer.group_send(
                self.campaign_group_name,
                {
                    'type': 'move_token',
                    'token_id': token_id,
                    'position_x': position_x,
                    'position_y': position_y
                }
            )
        elif action == 'delete_token':
            token_id = data.get('token_id')
            await self.delete_token(token_id)

    async def load_map(self, event):
        map_id = event['map_id']
        await self.send(text_data=json.dumps({
            'action': 'load_map',
            'map_id': map_id
        }))

    async def move_token(self, event):
        token_id = event['token_id']
        position_x = event['position_x']
        position_y = event['position_y']
        await self.send(text_data=json.dumps({
            'action': 'move_token',
            'token_id': token_id,
            'position_x': position_x,
            'position_y': position_y
        }))

    @database_sync_to_async
    def delete_token_sync(self, token_id):
        try:
            token = Token.objects.get(id=token_id)
            token.delete()
           # print(f"Token {token_id} deleted.")  # Adicione log para verificar a exclusão
            return token_id
        except Token.DoesNotExist:
         #   print(f"Token {token_id} does not exist.")  # Log para verificar se o token foi encontrado
            return None  # Token não existe

    async def delete_token(self, token_id):
        deleted_token_id = await self.delete_token_sync(token_id)
        if deleted_token_id is not None:
          #  print(f"Token {deleted_token_id} deleted and notifying group.")  # Adicione este log
            await self.channel_layer.group_send(
                self.campaign_group_name,
                {
                    'type': 'token_deleted',
                    'token_id': deleted_token_id
                }
            )

    async def token_deleted(self, event):
        token_id = event['token_id']
        await self.send(text_data=json.dumps({
            'action': 'delete_token',
            'token_id': token_id,
            'hide': True  # Incluímos uma flag para ocultar apenas o token deletado
        }))