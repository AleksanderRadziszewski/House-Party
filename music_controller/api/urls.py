from django.urls import path
from .views import RoomView
# from . import views

urlpatterns = [
    path('api', RoomView.as_view() ),
]