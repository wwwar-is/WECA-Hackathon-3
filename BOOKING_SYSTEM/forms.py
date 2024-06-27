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


# Bookings test -----------------------------------------------------------------------------------------

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['name', 'contact', 'email', 'event_type', 'guests', 'address', 'date']
        widgets = {
            'date': forms.Select(choices=[
                ('2023-07-01', 'July 1, 2023'),
                ('2023-07-02', 'July 2, 2023'),
                ('2023-07-03', 'July 3, 2023'),
                ('2023-07-04', 'July 4, 2023'),
                # Add more options as needed
            ])
        }
        