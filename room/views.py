from django.shortcuts import render,redirect
from .models import Room,Topic
from .forms import RoomForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
def room_page(request):
    q= request.GET.get('q') if request.GET.get('q') != None else ''
    rooms = Room.objects.filter(Q(topic__name__icontains = q)|
                                Q(name__icontains=q)|
                                Q(description__icontains=q)
                                ) 
    topics = Topic.objects.all()
    room_count = rooms.count()
    context = {'rooms':rooms ,'topics':topics, 'room_count':room_count}
    return render(request, 'Rooms.html',context)


def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username = username)
        except:
            messages.error(request, "Username does not exist.")

        user = authenticate(request, username=username , password=password)

        if user is not None:
            login(request, user)
            return redirect('rooms')
        else:
            messages.error(request, 'Username and Password does not exist!!')

    return render(request,'login_registration.html')

def LogOut_user(request):
    logout(request)
    return redirect('home')

@login_required(login_url='login')
def get_room(request,pk):
    room = Room.objects.get(id=pk)
    
    context = {'room':room}
    return render(request ,'room.html',context )

@login_required(login_url='login')
def create_room(request):
    form = RoomForm()
    if request.method == 'POST': 
        form = RoomForm(request.POST)  

        if form.is_valid():
            form.save()
            return redirect('rooms')

    context = {'form': form}
    return render(request, 'Createroom.html', context)


@login_required(login_url='login')
def update_room(request,pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)

    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid:
            form.save()
            return redirect('rooms')
        

    context= {'form':form}
    return render(request, 'Createroom.html',context)


@login_required(login_url='login')   
def deleteRoom(request,pk):
    room = Room.objects.get(id=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('rooms')
    return render(request ,'delete.html', {'obj':room})