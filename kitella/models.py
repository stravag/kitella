import uuid
from django.db import models


class Player(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    birthday = models.DateField

    def __str__(self):
        return self.email


class Event(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True)
    players = models.ManyToManyField(Player, blank=True)

    def __str__(self):
        return self.name


class Classification(models.Model):
    classified_player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='classified_player_id')
    classifying_player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='classifying_player_id')
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    val = models.DecimalField(max_digits=2, decimal_places=1)

    class Meta:
        unique_together = ('classified_player', 'classifying_player', 'event')

    def __str__(self):
        return self.val.__str__()
