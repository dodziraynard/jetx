from django import forms
from .models import (
    Location,
    Bus,
    Payment,
    Schedule,
    Booking,
)


class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        exclude = ["created_at"]


class BusForm(forms.ModelForm):
    class Meta:
        model = Bus
        exclude = ["created_at"]


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        exclude = ["created_at"]


class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        exclude = ["created_at", "active"]


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        exclude = ["created_at"]
