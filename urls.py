from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from . import views


urlpatterns = [
    path("",views.chat_hall, name="hall"),
    path('<str:room_name>/<str:user_name>',views.chat_room, name="room"),
    
]
