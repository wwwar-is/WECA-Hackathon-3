from django.contrib import admin
from .models import Customer, Booking, Payment, Review

# Register your models here.

admin.site.register(Customer)
admin.site.register(Booking)
admin.site.register(Payment)
admin.site.register(Review)