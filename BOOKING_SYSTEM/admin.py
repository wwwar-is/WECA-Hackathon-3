from django.contrib import admin
from .models import Customer, Booking, Payment, Review, AvailableDate

# Register your models here.
admin.site.register(Customer)
admin.site.register(Payment)
admin.site.register(Review)

class BookingAdmin(admin.ModelAdmin):
    list_display = ('get_customer_username', 'booking_date', 'status')
    list_filter = ('status', 'booking_date')
    actions = ['accept_bookings', 'decline_bookings', 'cancel_bookings']

    def get_customer_username(self, obj):
        return obj.user.user.username
    get_customer_username.admin_order_field = 'user'
    get_customer_username.short_description = 'Customer Username'

    def accept_bookings(self, request, queryset):
        queryset.update(status='confirmed')
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

admin.site.register(Booking, BookingAdmin)

class AvailableDateAdmin(admin.ModelAdmin):
    list_display = ('date',)
    actions = ['add_dates', 'delete_selected']

    def add_dates(self, request, queryset):
        # Custom action to add multiple dates
        self.message_user(request, "New dates can be added via the 'Add Available Date' button.")
    add_dates.short_description = "Add new available dates"

    def get_urls(self):
        from django.urls import path
        urls = super().get_urls()
        custom_urls = [
            path('add-dates/', self.admin_site.admin_view(self.add_dates_view), name='add-dates'),
        ]
        return custom_urls + urls

    def add_dates_view(self, request):
        from django import forms
        class AddMultipleDatesForm(forms.Form):
            dates = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

        if request.method == 'POST':
            form = AddMultipleDatesForm(request.POST)
            if form.is_valid():
                dates = form.cleaned_data['dates']
                for date in dates:
                    AvailableDate.objects.create(date=date)
                self.message_user(request, "Dates have been added.")
                return redirect('admin:app_availabledate_changelist')
        else:
            form = AddMultipleDatesForm()
        context = dict(
            self.admin_site.each_context(request),
            form=form,
        )
        return render(request, 'admin/add_dates.html', context)

admin.site.register(AvailableDate, AvailableDateAdmin)
