from django.shortcuts import get_object_or_404, redirect, render
from dashboard.utils import staff_only
from dashboard.models import Booking, Bus, Location, Notification, NotificationReading, Payment, Schedule
from django.utils.timezone import make_aware
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


@login_required(login_url="account:login")
def index(request):
    buses = Bus.objects.all()
    locations = Location.objects.all()
    bookings = Booking.objects.all()
    schedules = Schedule.objects.all()
    notifications = Notification.objects.all()
    users = User.objects.all()

    if request.user.is_staff:
        template_name = "dashboard/index.html"
        context = {
            "buses":buses,
            "locations":locations,
            "bookings":bookings,
            "schedules":schedules,
            "notifications":notifications,
            "users":users,
        }
    else:
        template_name = "client/dashboard/index.html"
        payments = Payment.objects.all()

        context = {
            "bookings":bookings,
            "schedules":schedules,
            "payments":payments,
        }
    return render(request, template_name, context)

# Locations
@staff_only
def locations(request):
    template_name = "dashboard/locations/locations.html"
    locations = Location.objects.all()
    context = {
        "locations":locations,
    }
    return render(request, template_name, context)

@staff_only
def store_location(request):
    template_name = "dashboard/locations/location_form.html"

    if request.method == "POST":
        id = request.POST.get("id")
        name = request.POST.get("name")
        if id:
            Location.objects.filter(id=id).update(name=name)
        else:
            Location.objects.create(name=name)

        return redirect("dashboard:locations")

    return render(request, template_name)

@staff_only
def edit_location(request, location_id):
    template_name = "dashboard/locations/location_form.html"
    location = get_object_or_404(Location, id = location_id)
    context = {
        "name":location.name,
        "id":location.id
    }
    return render(request, template_name, context)

@staff_only
def delete_location(request, location_id):
    Location.objects.filter(id=location_id).delete()
    request.message = "Location deleted successfully."
    redirect_url = request.META.get("HTTP_REFERER") or "dashboard:index"
    return redirect(redirect_url)

# Buses
@staff_only
def buses(request):
    template_name = "dashboard/buses/buses.html"
    buses = Bus.objects.all()
    context = {
        "buses":buses,
    }
    return render(request, template_name, context)

@staff_only
def store_bus(request):
    template_name = "dashboard/buses/bus_form.html"

    if request.method == "POST":
        id = request.POST.get("id")
        name = request.POST.get("name")
        number = request.POST.get("number")
        capacity = request.POST.get("capacity")
        if id:
            Bus.objects.filter(id=id).update(
                name=name,
                number=number,
                capacity=capacity,
            )
        else:
            Bus.objects.create(
                name=name,
                number=number,
                capacity=capacity,
            )
        return redirect("dashboard:buses")

    return render(request, template_name)

@staff_only
def edit_bus(request, bus_id):
    template_name = "dashboard/buses/bus_form.html"
    bus = get_object_or_404(Bus, id = bus_id)
    context = {
        "number":bus.number,
        "capacity":bus.capacity,
        "name":bus.name,
        "id":bus.id
    }
    return render(request, template_name, context)

@staff_only
def delete_bus(request, bus_id):
    Bus.objects.filter(id=bus_id).delete()
    request.message = "Bus deleted successfully."
    redirect_url = request.META.get("HTTP_REFERER") or "dashboard:index"
    return redirect(redirect_url)

# Schedules
@login_required(login_url="account:login")
def schedules(request):
    schedules = Schedule.objects.all()
    if request.user.is_staff:
        template_name = "dashboard/schedules/schedules.html"
    else:
        template_name = "client/dashboard/schedules/schedules.html"
    context = {
        "schedules":schedules,
    }
    return render(request, template_name, context)

@staff_only
def store_schedule(request):
    template_name = "dashboard/schedules/schedule_form.html"

    if request.method == "POST":
        id = request.POST.get("id")
        source_id = request.POST.get("source")
        source = Location.objects.get(id=source_id)
        price = request.POST.get("price")
        destination_id = request.POST.get("destination")
        destination = Location.objects.get(id=destination_id)
        bus_id = request.POST.get("bus")
        bus = Bus.objects.get(id=bus_id)
        departure_time = request.POST.get("departure_time")
        eta = request.POST.get("eta")


        departure_time = make_aware(datetime.fromisoformat(departure_time))
        eta = make_aware(datetime.fromisoformat(eta))

        if id:
            Schedule.objects.filter(id=id).update(
                source=source,
                destination=destination,
                price=price,
                bus=bus,
                departure_time=departure_time,
                eta=eta,
            )
        else:
            Schedule.objects.create(
                source=source,
                destination=destination,
                price=price,
                bus=bus,
                departure_time=departure_time,
                eta=eta,
            )
        return redirect("dashboard:schedules")
    else:
        locations = Location.objects.all()
        buses = Bus.objects.all()
        context = {
            "locations":locations,
            "buses":buses,
        }
        return render(request, template_name, context)

@staff_only
def edit_schedule(request, schedule_id):
    template_name = "dashboard/schedules/schedule_form.html"
    schedule = get_object_or_404(Schedule, id=schedule_id)
    locations = Location.objects.all()
    buses = Bus.objects.all()

    context = {
       "schedule":schedule,
        "locations":locations,
        "buses":buses,
    }
    return render(request, template_name, context)

@staff_only
def delete_schedule(request, schedule_id):
    Schedule.objects.filter(id=schedule_id).delete()
    request.message = "Schedule deleted successfully."
    redirect_url = request.META.get("HTTP_REFERER") or "dashboard:index"
    return redirect(redirect_url)

# Notification
@staff_only
def notifications(request):
    template_name = "dashboard/notifications/notifications.html"
    notifications = Notification.objects.all()
    context = {
        "notifications":notifications,
    }
    return render(request, template_name, context)

@staff_only
def store_notification(request):
    template_name = "dashboard/notifications/notification_form.html"

    if request.method == "POST":
        id = request.POST.get("id")
        category = request.POST.get("category")
        message = request.POST.get("message")
        if id:
            Notification.objects.filter(id=id).update(
                category=category,
                message=message,
            )
        else:
            Notification.objects.create(
                category=category,
                message=message,
                created_by=request.user,
            )
        return redirect("dashboard:notifications")

    return render(request, template_name)

@staff_only
def edit_notification(request, notification_id):
    template_name = "dashboard/notifications/notification_form.html"
    notification = get_object_or_404(Notification, id = notification_id)
    context = {
        "message":notification.message,
        "category":notification.category,
        "id":notification.id
    }
    return render(request, template_name, context)

@staff_only
def delete_notification(request, notification_id):
    Notification.objects.filter(id=notification_id).delete()
    request.message = "Notification deleted successfully."
    redirect_url = request.META.get("HTTP_REFERER") or "dashboard:index"
    return redirect(redirect_url)

@staff_only
def mark_notification_as_read(request, notification_id):
    notification = get_object_or_404(Notification, id=notification_id)
    NotificationReading.objects.get_or_create(
        read_by = request.user,
        notification = notification,
    )
    redirect_url = request.META.get("HTTP_REFERER") or "dashboard:index"
    return redirect(redirect_url)


# Payments
@login_required(login_url="account:login")
def payments(request):
    template_name = "dashboard/payments/payments.html"
    if request.user.is_staff:
        template_name = "dashboard/payments/payments.html"
        payments = Payment.objects.all()
    else:
        template_name = "client/dashboard/payments/payments.html"
        payments = Payment.objects.filter(user=request.user)
    context = {
        "payments":payments,
    }
    return render(request, template_name, context)

# Bookings
@login_required(login_url="account:login")
def bookings(request):
    if request.user.is_staff:
        template_name = "dashboard/bookings/bookings.html"
        bookings = Booking.objects.all()
    else:
        template_name = "client/dashboard/bookings/bookings.html"
        bookings = Booking.objects.filter(user=request.user)    
    
    context = {
        "bookings":bookings,
    }
    return render(request, template_name, context)