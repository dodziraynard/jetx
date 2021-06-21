from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.timezone import make_aware
from dashboard.models import Booking, Location, Payment, Schedule
from time import sleep


def index(request):
    template_name = "client/home.html"
    context = {
        "locations":Location.objects.all()
    }
    return render(request, template_name, context)


def get_schedules(request):
    template_name = "client/available_schedules.html"
    if request.method == "POST":
        source_id = request.POST.get("source_id")
        destination_id = request.POST.get("destination_id")
        departure_date = request.POST.get("departure_date")
        source = Location.objects.get(id=source_id)
        destination = Location.objects.get(id=destination_id)

        departure_time = make_aware(datetime.fromisoformat(departure_date))
        schedules = Schedule.objects.filter(source = source, destination = destination, departure_time__gte = departure_time)
        context = {
            "from":schedules.first().source if schedules.first() else None,
            "to":schedules.first().destination if schedules.first() else None,
            "schedules":schedules
        }
        return render(request, template_name, context)
    return redirect("client:index")

def schedule_details(request, schedule_id):
    template_name = "client/schedule_details.html"
    schedule = get_object_or_404(Schedule, id=schedule_id)

    context = {
        'schedule':schedule,
    }
    return render(request, template_name, context)

@login_required(login_url="account:login")
def make_payment(request, schedule_id):
    template_name = "client/make_payment.html"
    schedule = get_object_or_404(Schedule, id=schedule_id)

    context = {
        'schedule':schedule,
    }
    return render(request, template_name, context)

@login_required(login_url="account:login")
def payment_info(request, schedule_id):
    template_name = "client/payment_info.html"
    schedule = get_object_or_404(Schedule, id=schedule_id)

    amount = schedule.price
    number = request.POST.get("number")
    payment_method = request.POST.get("payment_method")

    payment = Payment.objects.create(amount=amount, user=request.user, number=number, method=payment_method)
    Booking.objects.create(
        user = request.user,
        payment = payment,
        schedule = schedule,
    )

    # Simulate payment processing
    sleep(5)
    context = {
        'schedule':schedule,
    }
    return render(request, template_name, context)