from django.utils import timezone
from rest_framework import status
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response

from bookings.models import Book
from rooms.models import Room
from rooms.serializers import RoomSerializer
from utils.paginations import CustomPageNumberPagination


class RoomListView(ListAPIView):
    queryset = Room.objects.order_by("-id")
    serializer_class = RoomSerializer
    filter_backends = (SearchFilter,)
    search_fields = ("name", "type")
    pagination_class = CustomPageNumberPagination


class RoomDetailView(RetrieveAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

    def retrieve(self, request, *args, **kwargs):
        room = Room.objects.filter(id=kwargs.get("pk")).first()
        if not room:
            return Response({"error": "topilmadi"}, status=status.HTTP_404_NOT_FOUND)
        return super().retrieve(request, *args, **kwargs)


class RoomAvailablityView(ListAPIView):
    def list(self, request, *args, **kwargs):
        room_id = kwargs.get("pk")
        today = timezone.now()
        data = []
        bookings = (
            Book.objects.filter(room_id=room_id, start__date=today.date(), end__date=today.date())
            .order_by("start").values("resident__name", "start__hour", "end__hour")
        )
        if bookings:
            first_booking_start_hour = bookings[0].get("start__hour") if bookings else 23
            if 9 <= first_booking_start_hour:
                data.append({
                    "resident": bookings[0].get("resident__name"),
                    "start": "9:00",
                    "end": f"{first_booking_start_hour}:00"
                })

            for i in range(len(bookings) - 1):
                start_hour = bookings[i].get("end__hour")
                end_hour = bookings[i + 1].get("start__hour")
                if start_hour != end_hour:
                    data.append({
                        "resident": bookings[i].get("resident_name"),
                        "start": f"{start_hour}:00",
                        "end": f"{end_hour}:00"
                    })

        last_booking_end_hour = bookings.last().get("end__hour") if bookings else 9
        if last_booking_end_hour <= 23:
            data.append({
                "resident": bookings.last().get("resident__name"),
                "start": f"{last_booking_end_hour}:00",
                "end": "23:00"
            })

        return Response(data)
