from django.contrib import admin


from .models import Player, Event, Classification


admin.site.register(Player)
admin.site.register(Event)
admin.site.register(Classification)
