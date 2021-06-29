# chat/consumers.py
import json,threading
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async

from .models import UsersConnected
from .chess_backend import string_to_numpy, get_fen



class ChatConsumer(AsyncWebsocketConsumer):
    """
    def __init__(self):
        user = 
    """

    async def connect(self):
        print(self.scope)
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.user_name = self.scope['url_route']['kwargs']['user_name']
        self.room_group_name = 'chat_%s' % self.room_name
        

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        print("JoinRoom - ",self.user_name)

        
        

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
        print("LeaveRoom - ",self.user_name)
        #chat_message({})

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        print("JSON:",text_data_json)
        if text_data_json["type"] == "message":
            message = f"{text_data_json['username']}: {text_data_json['message']}"

            # Send message to room group
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'chat_message',
                    'message': message
                }
            )
        elif text_data_json["type"] == "movement":
            # Calculate FEN code equivalent for this position
            board = string_to_numpy(text_data_json['fen'])
            fen,t = get_fen(board,"w")
            print(fen)
            print("AAAAAAAAAAAAAAAAAAAAAA")
            # Send message to room group
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'movement',
                    'n' : text_data_json['n'],
                    'n_eaten' : text_data_json['n_eaten'],
                    'next_turn' : text_data_json['next_turn'],
                    'fen' : fen,
                    'piece' : text_data_json['piece'],
                    'to' : text_data_json['to'],
                    'castle' : text_data_json['castle'],
                    'eat' : text_data_json['eat'],
                    'crown' : text_data_json['crown'],
                    'check' : text_data_json['check'],
                    'passant' : text_data_json['passant']

                    
                    
                }
            )
        elif text_data_json["type"] == "gamebegins":
            # Send message to room group
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'gamebegins',           
                    'opponent': text_data_json["opponent"],           
                }
            )

        elif text_data_json["type"] == "gamefinished":
            

            # Send message to room group
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'gamefinished',           
                    'winner' : text_data_json["winner"],
                    'reason' : text_data_json["reason"],      
                }
            )

    # Receive message from room group
    async def chat_message(self, event):
        print("EVENT: ",event)
        if event["type"] == 'chat_message':
    
            message = event['message']
            

            # Send message to WebSocket
            await self.send(text_data=json.dumps({
                'type': 'chat_message',
                'message': message
            }))

    async def movement(self, event):
        print("EVENT: ",event)
        
        

        if event["type"] == 'movement':
            await self.send(text_data=json.dumps({
                'type': 'movement',
                'n': event["n"],
                'n_eaten': event["n_eaten"],
                'next_turn': event["next_turn"],
                'fen': event["fen"],
                'piece': event["piece"],
                'to': event["to"],
                'castle' : event['castle'],
                'eat' : event['eat'],
                'crown' : event['crown'],
                'check' : event['check'],
                'passant' : event['passant'],
            }))

    async def gamebegins(self, event):
        print("EVENT: ",event)
        

        if event["type"] == 'gamebegins':
            await self.send(text_data=json.dumps({
                'type': 'gamebegins',
                'opponent': event["opponent"],
            }))

    async def gamefinished(self, event):
        print("EVENT: ",event)
        

        if event["type"] == 'gamefinished':
            await self.send(text_data=json.dumps({
                'type': 'gamefinished',
                'winner' : event["winner"],
                'reason' : event["reason"],
            }))

    
