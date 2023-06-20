from rest_framework import serializers
from bookings.models import Book, Resident


class ResidentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resident
        fields = ("id", "name", "phone", "email")


class BookSerializer(serializers.ModelSerializer):
    resident = ResidentSerializer()

    class Meta:
        model = Book
        fields = ("id", "resident", "room", "start", "end", "created_at", "updated_at")
