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
        action = data['action']

        if action == 'load_map':
            map_id = data['map_id']

            await self.channel_layer.group_send(
                self.campaign_group_name,
                {
                    'type': 'load_map',
                    'map_id': map_id
                }
            )
        elif action == 'move_token':
            token_id = data['token_id']
            position_x = data['position_x']
            position_y = data['position_y']

            await self.channel_layer.group_send(
                self.campaign_group_name,
                {
                    'type': 'move_token',
                    'token_id': token_id,
                    'position_x': position_x,
                    'position_y': position_y
                }
            )

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
