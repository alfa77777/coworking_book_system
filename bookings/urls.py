from django.urls import path
from bookings.views import ResidentListView, ResidentDetailView, BookCreateView, BookDetailView, BookListView

urlpatterns = [
    path("residents/", ResidentListView.as_view(), name="resident_list"),
    path("residents/<int:pk>/", ResidentDetailView.as_view(), name="resident_detail"),
    path("books/", BookListView.as_view(), name="book_list"),
    path("books/<int:pk>/", BookDetailView.as_view(), name="book_detail"),
    path("books/create/", BookCreateView.as_view(), name="book_create"),
]
