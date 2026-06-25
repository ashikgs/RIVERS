from django.db import models



class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.email


class Booking(models.Model):
    ROOM_CHOICES = [
        ('single', 'Single'),
        ('double', 'Double'),
        ('suite', 'Suite'),
    ]

    PAYMENT_METHODS = [
        ('GPay', 'Google Pay'),
        ('Cash', 'Cash on Arrival'),
    ]
    hotel_name = models.CharField(max_length=100, default='Hotel Unknown')

    name = models.CharField(max_length=100)
    email = models.EmailField()
    checkin = models.DateField()
    checkout = models.DateField()
    guests = models.PositiveIntegerField()
    room_type = models.CharField(max_length=10, choices=ROOM_CHOICES)
    payment_method = models.CharField(max_length=10, choices=PAYMENT_METHODS)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.name} - {self.room_type} - {self.checkin} to {self.checkout}"

class Hotel(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='hotel_images/')
    rating = models.FloatField()
    reviews = models.IntegerField()
    location = models.CharField(max_length=100)
    discount = models.CharField(max_length=50)
    booking_site = models.CharField(max_length=100)
    offer = models.CharField(max_length=100)
    price = models.IntegerField()
    date_range = models.CharField(max_length=50)

    def __str__(self):
        return self.name



