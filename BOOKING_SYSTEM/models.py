from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=254, unique=True, blank=False)
    phone_number = models.CharField(max_length=15, blank=False)

    def __str__(self):
        return self.user.username

class Booking(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    booking_location = models.CharField(max_length=255)
    booking_date = models.DateField()
    booking_time = models.TimeField()
    booking_length = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=[
            ('pending', 'Pending'),
            ('confirmed', 'Confirmed'),
            ('cancelled', 'Cancelled')
        ],
        default='pending'
    )

    def __str__(self):
        return f"{self.user.username} - on {self.booking_date} at {self.booking_time} for {self.booking_length}"
    
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


 # BOOKING MODELS TEST            

class Booking(models.Model):
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)
    email = models.EmailField()
    event_type = models.CharField(max_length=100)
    guests = models.PositiveIntegerField()
    address = models.CharField(max_length=255)
    date = models.DateField()

    def __str__(self):
        return f"{self.name} - {self.event_type} on {self.date}"
        
        return f"Review by {self.customer.username} for Booking {self.booking.id}" 

class AvailableDate(models.Model):
    date = models.DateField(unique=True)

    def __str__(self):
        return self.date.strftime('%Y-%m-%d')       
