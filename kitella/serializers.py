from .models import Event, Player
from rest_framework import serializers


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('url', 'id', 'name', 'description', 'players')
        depth = 1
        # TODO add AVG classification value to player obj (based on current event)
