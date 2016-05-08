from django.shortcuts import render, redirect, get_object_or_404


from .models import Event, Player, Classification


# Create your views here.
def index(request):
    events_list = Event.objects.order_by('name')
    context = {
        'events_list': events_list,
    }
    return render(request, 'events/index.html', context)


def create(request):
    # server side validation
    event = Event.objects.create(name=request.POST['name'], description=request.POST['description'])
    return redirect(event)


def detail(request, event_uuid):
    event = get_object_or_404(Event, pk=event_uuid)
    return render(request, 'events/detail.html', {'event': event})


def player_detail(request, event_uuid, player_uuid):
    event = get_object_or_404(Event, pk=event_uuid)
    player = get_object_or_404(Player, pk=player_uuid)

    # there has to be a better way than this, would prefer to use player object
    classifications = Classification.objects.filter(classified_player=player_uuid, event=event_uuid)

    context = {
        'event': event,
        'player': player,
        'classifications': classifications
    }

    return render(request, 'players/detail.html', context)
