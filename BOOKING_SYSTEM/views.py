from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .models import Customer, Booking, Payment, Review
from .forms import BookingForm
# Create your views here.

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
            return redirect('home')  # replace with your home URL or desired redirect URL
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

@login_required
def booking_view(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking_date = form.cleaned_data['booking_date']
            booking_time = form.cleaned_data['booking_time']
            booking_length = form.cleaned_data['booking_length']
            # Check if the time slot is available
            if Booking.objects.filter(booking_date=booking_date, booking_time=booking_time).exists():
                messages.error(request, 'This time slot is already booked. Please choose another time.')
            else:
                booking = form.save(commit=False)
                booking.user = request.user.customer  # assuming user is related to customer
                booking.save()
                messages.success(request, 'Your booking has been made successfully!')
                return redirect('booking_confirmation', booking_id=booking.id)
    else:
        form = BookingForm()
    return render(request, 'booking.html', {'form': form})

@login_required
def booking_confirmation_view(request, booking_id):
    booking = Booking.objects.get(id=booking_id)
    return render(request, 'booking_confirmation.html', {'booking': booking})

