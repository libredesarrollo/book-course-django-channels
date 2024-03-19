from django.shortcuts import render
from django.http.response import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def room(request, room_id):
    try:
        room = request.user.rooms_joined.get(id=room_id)
    except:
        return HttpResponseForbidden()
    
    return render(request, 'chat/room.html',{ 'room':room })
    