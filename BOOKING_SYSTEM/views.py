from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Customer, Booking, Payment, Review
# Create your views here.

def booking (request):
    return HttpResponse("hello world!")