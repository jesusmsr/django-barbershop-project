from django.db import models
from django.contrib.auth.models import User
from user_app.models import Account

# Create your models here.
class Booking(models.Model):
    booking_code = models.CharField(max_length=8)
    user = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='bookingUser')
    notes = models.CharField(max_length=255)
    active = models.BooleanField(default=True)
    booking_date = models.DateTimeField(default=None)
    duration = models.PositiveIntegerField(default=0)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.booking_code + ' '+self.user.username