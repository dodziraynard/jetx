from django.urls import path
from . import views

app_name = "client"

urlpatterns = [
    path('', views.index, name="index"),
    path('get_schedules', views.get_schedules, name="get_schedules"),
    path('schedule_details/<int:schedule_id>', views.schedule_details, name="schedule_details"),
    path('schedule_details/<int:schedule_id>/make_payment', views.make_payment, name="make_payment"),
    path('schedule_details/<int:schedule_id>/make_payment/payment_info', views.payment_info, name="payment_info"),
]