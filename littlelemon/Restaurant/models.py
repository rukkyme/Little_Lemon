from django.db import models
from datetime import datetime


# Create your models here.
class Booking(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField()
    booking_date = models.DateTimeField(default=datetime.now)
    
    def __str__(self):
        return f"{self.name} - Guests {self.no_of_guests} \n {self.booking_date}"
    

class Menu(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    inventory = models.IntegerField()
    
    def __str__(self):
        return f"{self.title} - price: {self.price}"
    