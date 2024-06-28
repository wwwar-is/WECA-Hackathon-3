from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin

# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=254, unique=True, blank=False)
    phone_number = models.CharField(max_length=15, blank=False)

    def __str__(self):
        return self.user.username

class Booking(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    booking_date = models.DateField()
    booking_time = models.TimeField()
    booking_length = models.PositiveIntegerField()
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    email = models.EmailField()
    event_type = models.CharField(max_length=100)
    number_guests = models.PositiveIntegerField()
    address = models.CharField(max_length=255)


    def __str__(self):
        return f"Booking for {self.name} on {self.booking_date} at {self.booking_time}"
    
class Payment(models.Model):
    booking = models.OneToOneField(Booking, on_delete=models.CASCADE)
    transaction_id = models.CharField(max_length=100, unique=True)
    quote = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(
        max_length=20,
        choices=[
            ('pending', 'Pending'),
            ('completed', 'Completed'),
            ('failed', 'Failed')
        ],
        default='pending'
    )

    def __str__(self):
        return f"Payment for Booking {self.booking.id} - {self.status}"

class Review(models.Model):
    booking = models.OneToOneField(Booking, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()
    comment = models.TextField(blank=True, max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.customer.username} for Booking {self.booking.id}" 

class AvailableDate(models.Model):
    date = models.DateField(unique=True)

    def __str__(self):
        return self.date.strftime('%Y-%m-%d')       