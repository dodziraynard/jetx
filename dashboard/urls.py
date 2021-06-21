from django.urls import path
from . import views

app_name = "dashboard"

urlpatterns = [
    path('', views.index, name="index"),
    path('store_location', views.store_location, name="store_location"),
    path('edit_location/<int:location_id>', views.edit_location, name="edit_location"),
    path('delete_location/<int:location_id>', views.delete_location, name="delete_location"),
    path('locations', views.locations, name="locations"),

    path('store_bus', views.store_bus, name="store_bus"),
    path('edit_bus/<int:bus_id>', views.edit_bus, name="edit_bus"),
    path('delete_bus/<int:bus_id>', views.delete_bus, name="delete_bus"),
    path('buses', views.buses, name="buses"),

    path('store_schedule', views.store_schedule, name="store_schedule"),
    path('edit_schedule/<int:schedule_id>', views.edit_schedule, name="edit_schedule"),
    path('delete_schedule/<int:schedule_id>', views.delete_schedule, name="delete_schedule"),
    path('schedules', views.schedules, name="schedules"),

    path('store_notification', views.store_notification, name="store_notification"),
    path('edit_notification/<int:notification_id>', views.edit_notification, name="edit_notification"),
    path('delete_notification/<int:notification_id>', views.delete_notification, name="delete_notification"),
    path('mark_notification_as_read/<int:notification_id>', views.mark_notification_as_read, name="mark_notification_as_read"),
    path('notifications', views.notifications, name="notifications"),

    path('payments', views.payments, name="payments"),
    path('bookings', views.bookings, name="bookings"),
]

