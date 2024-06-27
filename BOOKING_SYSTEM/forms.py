from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['booking_location', 'booking_date', 'booking_time', 'booking_length']
        widgets = {
            'booking_date': forms.DateInput(attrs={'type': 'date'}),
            'booking_time': forms.TimeInput(attrs={'type': 'time'}),
            'booking_length': forms.TextInput(attrs={'placeholder': 'e.g., 1 hour'}),
        }