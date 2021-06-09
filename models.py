from django.db import models

import datetime

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
