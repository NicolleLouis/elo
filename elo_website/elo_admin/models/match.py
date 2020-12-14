from django.contrib import admin
from django.db import models
from django.db.models import SET_NULL
from django.db.models.signals import post_save
from django.dispatch import receiver

from elo_admin.models.player import Player


class Match(models.Model):
    id = models.AutoField(
        primary_key=True,
    )
    winner_player = models.ForeignKey(
        Player,
        related_name="winner",
        on_delete=SET_NULL,
        null=True
    )
    loser_player = models.ForeignKey(
        Player,
        related_name="loser",
        on_delete=SET_NULL,
        null=True
    )


@receiver(post_save, sender=Match, dispatch_uid="update_elo")
def update_elo(sender, instance, **kwargs):
    ## Constants ##
    max_delta_elo = 50
    ## Constants ##

    winner = instance.winner_player
    loser = instance.loser_player
    winner_elo = winner.elo
    loser_elo = loser.elo

    elo_difference = winner_elo - loser_elo
    if elo_difference > 500:
        elo_difference = 500
    elif elo_difference < -500:
        elo_difference = -500
    delta_elo = max_delta_elo * (1 - (0.5 + elo_difference / 1000))

    winner.elo = winner.elo + delta_elo
    loser.elo = loser.elo - delta_elo

    winner.save()
    loser.save()


class MatchAdmin(admin.ModelAdmin):
    list_display = (
        'winner_player',
        'loser_player'
    )
