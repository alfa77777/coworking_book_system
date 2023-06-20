from django.urls import path

from rooms.views import RoomListView, RoomDetailView, RoomAvailablityView

urlpatterns = [
    path("", RoomListView.as_view(), name="rooms_list"),
    path("<int:pk>/", RoomDetailView.as_view(), name="room_detail"),
    path("<int:pk>/availability/", RoomAvailablityView.as_view(), name="room_availabilty"),
]
