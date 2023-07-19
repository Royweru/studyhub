from django.shortcuts import render,redirect
from .models import Room,Topic
from .forms import RoomForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.db.models import Q
def room_page(request):
    q= request.GET.get('q') if request.GET.get('q') != None else ''
    rooms = Room.objects.filter(Q(topic__name__icontains = q)|
                                Q(name__icontains = q)|
                                Q(description__icontains = q)
                                ) 
    topics = Topic.objects.all()
    room_count = rooms.count()
    context = {'rooms':rooms ,'topics':topics, 'room_count':room_count}
    return render(request, 'components/Rooms.html',context)


def LoginPage(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect('rooms')

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
    context = {'page':page}
    return render(request,'components/login_registration.html', context)

def LogOut_user(request):
    logout(request)
    return redirect('home')


def registerPage(request):
    page = 'register'
    form = UserCreationForm()


    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid:
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('rooms')
        else:
            messages.error(request, 'An error occured during registration')

    context = {'page':page, 'form':form}
    return render(request, 'components/login_registration.html',context)

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
    
    if request.user != room.host:
        return HttpResponse(f"Get the fuck out of {room.host}'s room please" )

    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid:
            form.save()
            return redirect('rooms')
        

    context= {'form':form}
    return render(request, 'components/Createroom.html',context)


@login_required(login_url='login')   
def deleteRoom(request,pk):
    room = Room.objects.get(id=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('rooms')
    return render(request ,'components/delete.html', {'obj':room})