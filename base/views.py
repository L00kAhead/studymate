from django.shortcuts import render
from .models import Room

# Create your views here.

# rooms = [
#     {"id": 1, "name": "UI/UX principles"},
#     {"id": 2, "name": "Natural Language Processing"},
# ]


def home(request):
    rooms = Room.objects.all()
    return render(request, "base/home.html", {"rooms": rooms})


def room(request, pk):
    room = Room.objects.get(id=pk)
    context = {"room": room}
    return render(request, "base/room.html", context)
