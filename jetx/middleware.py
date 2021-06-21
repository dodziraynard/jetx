from dashboard.models import Notification, NotificationReading


class CustomMiddleWares(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.message = request.session.pop("message", "")
        request.error_message = request.session.pop("error_message", "")
        
        if request.user.is_authenticated:
            category = "admins" if request.user.is_staff else "users"
            read_notifications = NotificationReading.objects.filter(read_by = request.user)
            read_ids = [item['notification'] for item in list(read_notifications.values("notification"))]
            notifications = Notification.objects.filter(category=category).exclude(
                id__in = read_ids
            )
            request.notifications = notifications
        return self.get_response(request)
