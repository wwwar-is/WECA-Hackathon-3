from django import forms
from .models import Booking
from .models import Customer

class BookingForm(forms.ModelForm):
    name = forms.CharField(max_length=100)
    contact = forms.CharField(max_length=100)
    email = forms.EmailField()
    event_type = forms.CharField(max_length=100)
    number_guests = forms.IntegerField()
    address = forms.CharField(max_length=255)
    booking_date = forms.DateField(widget=forms.SelectDateWidget)
    booking_time = forms.TimeField(widget=forms.TimeInput(format='%H:%M'))
    booking_length = forms.IntegerField()

    class Meta:
        model = Booking
        fields = ['name', 'contact', 'email', 'event_type', 'number_guests', 'address', 'booking_date', 'booking_time', 'booking_length']