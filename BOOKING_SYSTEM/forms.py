from django import forms
from .models import Booking, AvailableDate

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
        
class AddMultipleDatesForm(forms.Form):
    dates = forms.CharField(widget=forms.Textarea, help_text='Enter dates separated by commas')

    def clean_dates(self):
        dates_str = self.cleaned_data['dates']
        dates = [date.strip() for date in dates_str.split(',')]
        for date in dates:
            try:
                parsed_date = datetime.strptime(date, '%Y-%m-%d').date()
            except ValueError:
                raise forms.ValidationError(f"{date} is not a valid date.")
        return dates
