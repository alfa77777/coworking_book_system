from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView
from bookings.models import Book, Resident
from bookings.serializers import BookSerializer, ResidentSerializer


class ResidentListView(ListAPIView):
    queryset = Resident.objects.all()
    serializer_class = ResidentSerializer


class ResidentDetailView(RetrieveAPIView):
    queryset = Resident.objects.all()
    serializer_class = ResidentSerializer


class BookCreateView(CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDetailView(RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookListView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
