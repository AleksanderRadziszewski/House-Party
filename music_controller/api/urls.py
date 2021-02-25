from django.urls import path
from .views import RoomView, CreateRoomView
# from . import views

urlpatterns = [
    path('room', RoomView.as_view() ),
    path('create-room', CreateRoomView.as_view())
]