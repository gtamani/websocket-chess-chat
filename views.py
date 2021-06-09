from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from django.utils.safestring import mark_safe

import json

# Create your views here.

def chat_hall(request):
    user_name = request.POST.get("username")
    room_name = request.POST.get("roomname")
    if user_name:
        print(user_name)
        return redirect(f"/chat/{room_name}/{user_name}")
    return render(request,"chat_hall.html")

def chat_room(request,room_name,user_name):
    """
    new_user = UsersConnected(nick = user_name)
    new_user.save()

    users_connected = UsersConnected.objects.all()
    print(users_connected)
    """


    return render(request, "chat_room.html", 
    {'room_name': room_name,
    'user_name' : user_name,
    'board' : range(1,9),
    })

