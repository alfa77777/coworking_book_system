from django.contrib import admin

from bookings.models import Book, Resident


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass

@admin.register(Resident)
class ResidentAdmin(admin.ModelAdmin):
    pass
