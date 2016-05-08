from django.conf.urls import url

from . import views

app_name = 'events'
urlpatterns = [
    # ex: /events/
    url(r'^$', views.index, name='index'),

    # ex: /events/create
    url(r'^create$', views.create, name='create'),

    # ex: /events/123e4567-e89b-12d3-a456-426655440000/
    url(r'^(?P<event_uuid>[^/]+)/$', views.detail, name='event'),

    # ex: /events/<uuid>/players/<uuid>
    url(r'^(?P<event_uuid>[^/]+)/players/(?P<player_uuid>[^/]+)$', views.player_detail, name='player'),
]
