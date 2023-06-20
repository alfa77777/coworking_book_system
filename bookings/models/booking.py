from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _


class Book(models.Model):
    resident = models.ForeignKey("bookings.Resident", on_delete=models.CASCADE, related_name="bookings")
    room = models.ForeignKey("rooms.Room", on_delete=models.CASCADE, related_name="bookings")
    start = models.DateTimeField(_("Start date"))
    end = models.DateTimeField(_("End date"))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def clean(self):
        # Check if there is any existing booking for the same room and overlapping time period
        existing_booking = Book.objects.filter(room=self.room, start__lt=self.end, end__gt=self.start).exclude(
            pk=self.pk).first()
        if existing_booking:
            raise ValidationError(_("This room is already booked for the specified time period."))

    def __str__(self):
        return f"{self.resident} - {self.room}"
