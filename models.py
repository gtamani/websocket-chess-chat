from django.db import models


import datetime
import numpy as np

# Create your models here.

class Chat(models.Model):
    room_name = models.CharField(max_length=120)

    def __str__(self):
        return self.room_name

    def get_messages(self):
        self.messages.all()

class ChatMessage(models.Model):
    chat = models.ForeignKey(Chat,on_delete = models.CASCADE, related_name="messages")
    nick = models.CharField(max_length=120)
    text = models.TextField()
    date = models.DateField("Inicio de sesión",default=datetime.datetime.now())

    def __str__(self):
        return f"{self.chat.room_name} - {self.nick}"

class UsersConnected(models.Model):
    id = models.AutoField(primary_key=True)
    nick = models.CharField(max_length=120)
    connected = models.DateField("Fecha de Creación",default=datetime.datetime.now())

    def __str__(self):
        return self.nick

class Games(models.Model):
    hall_name = models.CharField(max_length = 20 )
    player1 = models.CharField(max_length = 50, default = np.nan )
    player2 = models.CharField(max_length = 50, default = np.nan )
    password = models.CharField(max_length = 20 )
    turn = models.CharField(max_length = 1, default= "w")
    player1_color = models.CharField(max_length = 1, default= "w")
    fen = models.CharField(max_length = 60, default= "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")
    time = models.IntegerField(default=10)
    def __str__(self):
        return f"{self.hall_name} - {self.player1} vs. {self.player2} "
    
