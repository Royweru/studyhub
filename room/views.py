from django.shortcuts import render
from .models import Room
def room_page(request):
    rooms = Room.objects.all() 
    context = {'rooms':rooms}
    return render(request, 'Rooms.html',context)


def getroom(request,pk):
    rooms = Room.objects.get(id=pk)
    context = {rooms:'rooms'}
    return render(request ,'room.html',context )
  