from .models import Event, Player
from rest_framework import viewsets
from .serializers import EventSerializer


class EventViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows events to be viewed or edited.
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer


# TODO POST method to add classification
# URL: /rest/events/{id}/players/{id}/classifications
# Body { value : 1.5 }

