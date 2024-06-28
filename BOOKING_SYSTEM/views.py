from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .models import Customer, Booking, Payment, Review, AvailableDate
from .forms import BookingForm
from django.contrib.auth.forms import AuthenticationForm

def index_view(request):
    return render(request, 'index.html')

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            login(request, user)
            return redirect('index')  # replace with your home URL or desired redirect URL
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def booking_view(request):
    # try:
    #     customer = request.user.customer
    # except Customer.DoesNotExist:
    #     return redirect('profile')  # Redirect to profile completion if customer does not exist

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking_date = form.cleaned_data['date']
            booking_time = form.cleaned_data['booking_time']
            booking_length = form.cleaned_data['booking_length']
            name = form.cleaned_data['name']
            contact = form.cleaned_data['contact']
            email = form.cleaned_data['email']
            event_type = form.cleaned_data['event_type']
            number_guests = form.cleaned_data['number_guests']
            address = form.cleaned_data['address']
            
            # Check if the time slot is available
            if Booking.objects.filter(booking_date=booking_date, booking_time=booking_time).exists():
                messages.error(request, 'This time slot is already booked. Please choose another time.')
            else:
                booking = form.save(commit=False)
                booking.customer = customer  # Assign the customer to the booking
                booking.name = name
                booking.contact = contact
                booking.email = email
                booking.event_type = event_type
                booking.number_guests = number_guests
                booking.address = address
                booking.save()
                messages.success(request, 'Your booking has been made successfully!')
                return redirect('booking_confirmation', booking_id=booking.id)
    else:
        form = BookingForm()

    return 
    render(request, 'booking.html', {'form': form})
    # HttpResponse (f'Booking for {'booking_time'} and {'date'} is complete you should recieve an email confirmation soon')
 

@login_required
def booking_confirmation_view(request, booking_id):
    booking = Booking.objects.get(id=booking_id)
    return render(request, 'booking_confirmation.html', {'booking': booking})

def add_dates_view(request):
    from django import forms
    class AddMultipleDatesForm(forms.Form):
        dates = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    if request.method == 'POST':
        form = AddMultipleDatesForm(request.POST)
        if form.is_valid():
            dates = form.cleaned_data['dates']
            for date in dates:
                AvailableDate.objects.create(date=date)
            messages.success(request, "Dates have been added.")
            return redirect('admin:app_availabledate_changelist')
    else:
        form = AddMultipleDatesForm()
    return render(request, 'admin/add_dates.html', {'form': form})
