from django.contrib import admin
from .models import Customer, Booking, Payment, Review, AvailableDate, Booking

# Register your models here.
admin.site.register(Customer)
admin.site.register(Booking)
admin.site.register(Payment)
admin.site.register(Review)

class BookingAdmin(admin.ModelAdmin):
    list_display = ('customer', 'date', 'status')
    list_filter = ('status', 'date')
    actions = ['accept_bookings', 'decline_bookings', 'cancel_bookings']

    def accept_bookings(self, request, queryset):
        queryset.update(status='accepted')
        self.message_user(request, "Selected bookings have been accepted.")
    accept_bookings.short_description = "Accept selected bookings"

    def decline_bookings(self, request, queryset):
        queryset.update(status='declined')
        self.message_user(request, "Selected bookings have been declined.")
    decline_bookings.short_description = "Decline selected bookings"

    def cancel_bookings(self, request, queryset):
        queryset.update(status='cancelled')
        self.message_user(request, "Selected bookings have been cancelled.")
    cancel_bookings.short_description = "Cancel selected bookings"

class AvailableDateAdmin(admin.ModelAdmin):
    list_display = ('date',)
    actions = ['add_dates', 'delete_selected']

    def add_dates(self, request, queryset):
        # Custom action to add multiple dates
        self.message_user(request, "New dates can be added via the 'Add Available Date' button.")
    add_dates.short_description = "Add new available dates"