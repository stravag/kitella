"""kitella URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [

    url(r'^events/?$', views.index, name='index'),
    url(r'^events/create$', views.create, name='create'),
    url(r'^events/(?P<event_uuid>[^/]+)/$', views.detail, name='event'),
    url(r'^events/(?P<event_uuid>[^/]+)/players/(?P<player_uuid>[^/]+)$', views.player_detail, name='player'),

    url(r'^admin/', admin.site.urls),
]
