from django.shortcuts import render, redirect
from .models import Room
from .forms import RoomForm
from . import urls

# rooms_data = [
#     {'id':1, 'name':'This is the room for Python beginners.'},
#     {'id':2, 'name':'This is the room for Competitive Programming beginners.'},
#     {'id':3, 'name':'This is the room for Data Structures and Algorithms beginners.'},
# ]


def home(request):
    rooms_data = Room.objects.all()
    context = {'rooms_data': rooms_data}
    return render(request, 'base/home.html', context)

def rooms(request, pk):
    # room = None
    # for i in rooms_data:
    #     if(i['id'] == int(pk)):
    #         room = i
    room = Room.objects.get(id=pk)
    context = {'room': room}
    return render(request, 'base/rooms.html', context)

def createRoom(request):
    room = RoomForm()
    if(request.method == 'POST'):
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("Home")

    context = {'room': room}
    return render(request, 'base/room_form.html', context)