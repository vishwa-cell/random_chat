

# Create your views here.
import uuid
from django.http import JsonResponse
from django.shortcuts import render, redirect

waiting_user = None   # global memory


def home(request):
    return render(request, "home.html")


def find_match(request):
    global waiting_user
    user_id = str(uuid.uuid4())  # assign guest id

    if waiting_user is None:
        # No one waiting
        waiting_user = user_id
        return JsonResponse({"status": "waiting", "user": user_id})

    else:
        # Someone is waiting → match
        partner = waiting_user
        waiting_user = None

        room = str(uuid.uuid4())
        return JsonResponse({
            "status": "matched",
            "room": room,
            "user": user_id,
            "partner": partner
        })


def chat_room(request, room):
    return render(request, "chat.html", {"room": room})
