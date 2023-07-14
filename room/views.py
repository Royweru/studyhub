from django.shortcuts import render
from .models import Room
from .forms import RoomForm
def room_page(request):
    rooms = Room.objects.all() 
    context = {'rooms':rooms}
    return render(request, 'Rooms.html',context)


def get_room(request,pk):
    room = Room.objects.get(id=pk)
    context = {'room':room}
    return render(request ,'room.html',context )
  
def create_room(request):
    form = RoomForm()
    context = {'form':form}
    return render(request, 'Createroom.html', context )