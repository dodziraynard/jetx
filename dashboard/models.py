from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


class Location(models.Model):
    name = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(default=now)

    def __repr__(self) -> str:
        return self.name

class Bus(models.Model):
    name = models.CharField(max_length=100)
    capacity = models.IntegerField()
    number = models.CharField(max_length=20)
    created_at = models.DateTimeField(default=now)

    def __repr__(self) -> str:
            return self.name

class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="payments")
    amount = models.DecimalField(max_digits=20, decimal_places=2)
    note = models.TextField()
    number = models.CharField(max_length=20)
    method = models.CharField(max_length=20)
    created_at = models.DateTimeField(default=now)

    def __repr__(self) -> str:
        return f"{self.user.username} - {self.amount}"
 
class Schedule(models.Model):
    departure_time = models.DateTimeField()
    eta = models.DateTimeField()
    price = models.DecimalField(max_digits=20, decimal_places=2)
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    source = models.ForeignKey(Location, on_delete=models.CASCADE, related_name="source_schedules")
    destination = models.ForeignKey(Location, on_delete=models.CASCADE, related_name="destination_schedules")
    created_at = models.DateTimeField(default=now)
    active = models.BooleanField(default=True)

    def available_capacity(self):
        return self.bus.capacity - self.bookings.count() 

    def __repr__(self) -> str:
            return f"{self.source.name} to {self.destination.name}"

class Booking(models.Model):
    payment = models.ForeignKey(Payment, null=True, blank=True, on_delete=models.SET_NULL)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bookings")
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE, related_name="bookings")
    created_at = models.DateTimeField(default=now)

    def __repr__(self) -> str:
        return f"{self.user.username}"

class Notification(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=100, default="users", choices=(("admins", "admins"), ("users", "users")))
    message = models.TextField()
    read = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=now)

    def __repr__(self) -> str:
        return f"{self.message}"

class NotificationReading(models.Model):
    notification = models.ForeignKey(Notification, on_delete=models.CASCADE)
    read_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='read_notifications')