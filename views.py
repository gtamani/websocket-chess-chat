from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from django.utils.safestring import mark_safe

from .models import Games
import json,random
import numpy as np


# Create your views here.

def chat_hall(request):
    device = request.POST.get("device")
    
    if device:
        try:
            user_name = request.POST.get("username"+device)
        except:
            username = None
        
        try:
            new_room_name = request.POST.get("new_roomname"+device)
        except:
            new_room_name = None
        
        room_name = request.POST.get("roomname"+device)
        password = request.POST.get("password"+device)
        time = request.POST.get("time"+device)

        print("AAAAAAAAAAAA",device)
        print("AAAAAAAAAAAA",user_name)
        print("AAAAAAAAAAAA",room_name)
        print("AAAAAAAAAAAA",new_room_name)

        # Create a room
        

        if user_name and (room_name or new_room_name):
            if room_name:
                hall = room_name if Games.objects.filter(hall_name=room_name) else new_room_name
            else:
                hall = new_room_name
            color = random.choice(["w","b"])

            print("HALL",hall)
            print(Games.objects.filter(hall_name=room_name))

            new_board = Games(
                hall_name=hall,
                player1=user_name,
                password=password,
                player1_color = color,
                time = time,
                
                )
            
            new_board.save()

            print(Games.objects.filter(hall_name=hall))

            return redirect(f"/chess/{hall}/{user_name}")
        return render(request,"chat_hall.html")
    return render(request,"chat_hall.html")

def chat_room(request,room_name,user_name):
    """
    new_user = UsersConnected(nick = user_name)
    new_user.save()

    users_connected = UsersConnected.objects.all()
    print(users_connected)
    """
    # Check if that room exists
    exists = Games.objects.filter(hall_name=room_name)
    print("BOARDDD", exists)
    print(room_name,user_name)


    print("EXISTS",exists)
    if exists:
        if exists[0].player2 == "nan":    
            if exists[0].player1 != user_name:
                print("Jugador 2")
                opponent_name = exists[0].player1
                color = exists[0].player1_color
                color = "w" if color == "b" else "b"
                exists.update(player2 = user_name)
                print(exists)
            else:
                # Create a room
                print("Jugador 1")
                opponent_name = np.nan
                color = exists[0].player1_color
                #new_board = Games(hall_name=room_name,player1=user_name,password=np.nan,player1_color = color)
                #new_board.save()

            #Common argues for both players
            password = exists[0].password
            timer = exists[0].time
            board = range(8,0,-1) if color == "b" else range(1,9)
            

            return render(request, "chat_room.html", 
            {'room_name': room_name,
            'user_name' : user_name,
            'password' : password,
            'opponent_name' : opponent_name,
            'color' : color,
            'board' : board,
            'board_st' : range(1,9),
            'time' : timer
            })

        else:
            return render(request,"room_fool.html")
    else:
        color = random.choice(["w","b"])
        new_board = Games(
            hall_name=room_name,
            player1=user_name,
            password="",
            player1_color = color,
            time = 10,
            
            
            )
        
        new_board.save()
        chat_room(request,room_name,user_name)
        return render(request,"404.html")
        

    

