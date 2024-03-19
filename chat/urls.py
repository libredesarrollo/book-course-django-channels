from django.urls import path

from .import views

urlpatterns = [
    path('room/<int:room_id>/',views.room, name='room'),
]
