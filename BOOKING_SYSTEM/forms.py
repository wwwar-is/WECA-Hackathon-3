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