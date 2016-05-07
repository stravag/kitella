from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Event, Player


# Create your views here.
def index(request):
    events_list = Event.objects.order_by('name')
    context = {
        'events_list': events_list,
    }
    return render(request, 'events/index.html', context)


def detail(request, event_uuid):
    event = get_object_or_404(Event, pk=event_uuid)
    return render(request, 'events/detail.html', {'event': event})


def players(request, event_uuid):
    return HttpResponse("You're looking at players of event %s." % event_uuid)


def player_detail(request, event_uuid, player_uuid):
    event = get_object_or_404(Event, pk=event_uuid)
    player = get_object_or_404(Player, pk=player_uuid)
    return render(request, 'players/detail.html', {'event': event, 'player': player})
