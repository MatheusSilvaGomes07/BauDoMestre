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

    async def load_map(self, event):
        map_id = event['map_id']

        await self.send(text_data=json.dumps({
            'action': 'load_map',
            'map_id': map_id
        }))
