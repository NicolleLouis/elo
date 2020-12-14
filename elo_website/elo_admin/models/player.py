from django.contrib import admin
from django.db import models


class Player(models.Model):
    id = models.AutoField(
        primary_key=True,
    )
    name = models.TextField(
        blank=True,
        null=True
    )
    elo = models.IntegerField(
        blank=True,
        null=True,
        default=1000
    )

    def __str__(self):
        return self.name


class PlayerAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "elo",
    ]
