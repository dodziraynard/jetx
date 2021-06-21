from django.shortcuts import redirect


def staff_only(function):
    def wrapper(request, *args, **kw):
        if not (request.user.is_staff):
            request.session['message'] = "Please login as as admin."
            return redirect("account:login")
        else:
            return function(request, *args, **kw)
    return wrapper