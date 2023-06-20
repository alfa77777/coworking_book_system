from django.db import models
from django.utils.translation import gettext_lazy as _


class Room(models.Model):
    class RoomTypes(models.TextChoices):
        FOCUS = "focus", _("Focus")
        TEAM = "team", _("Team")
        CONFERENCE = "conference", _("Conference")

    name = models.CharField(max_length=255)
    capacity = models.PositiveSmallIntegerField()
    type = models.CharField(max_length=50, choices=RoomTypes.choices)

    def __str__(self):
        return self.name
