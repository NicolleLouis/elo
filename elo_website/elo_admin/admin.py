import django.contrib.auth.models

from django.contrib import admin
from django.contrib import auth

from elo_admin.models.player import Player, PlayerAdmin
from elo_admin.models.match import Match, MatchAdmin

admin.site.register(Player, PlayerAdmin)
admin.site.register(Match, MatchAdmin)

admin.site.unregister(auth.models.User)
admin.site.unregister(auth.models.Group)
