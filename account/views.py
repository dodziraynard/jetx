from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.utils import timezone
from django.contrib.auth.models import User


def account_login(request):
    template_name = "account/accounts_login.html"
    context = {}

    if request.method == "POST":
        # Retrieving posted parameters.
        username = request.POST.get("username")
        password = request.POST.get("password")
        remember_me = True if request.POST.get("remember_me") else False
        user = authenticate(username=username, password=password)

        # If the credentials are correct, a user object will be returned.
        if user:
            login(request, user)
            if remember_me:
                # Increase the session expiration to 30 days.
                request.session.set_expiry(86400 * 30)
            user.last_login_date = timezone.now()
            user.save()
            redirect_url = request.GET.get("next") or "dashboard:index"
            return redirect(redirect_url)
        else:
            context.update({
                "error_message": "Invalid credentials",
                **{key:value[0] for key, value in dict(request.POST).items()},
            })
    return render(request, template_name, context)

def account_logout(request):
    redirect_url = request.META.get('HTTP_REFERER') or "dashboard:index"
    logout(request)
    return redirect(redirect_url)

def register(request):
    template_name = "account/accounts_register.html"
    context = {}

    if request.method == "POST":
        username = request.POST.get("username")
        full_name = request.POST.get("full_name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        
        # Split fullname into last name and first name.
        last_name = full_name.split()[0]
        first_name = " ".join(full_name.split()[1:])
        
        user = User.objects.create(username=username, last_name=last_name, first_name=first_name, email=email)

        if user:
            user.set_password(password)
            user.save()
            login(request, user)
            redirect_url = request.GET.get("next") or "dashboard:index"
            return redirect(redirect_url)
        else:
            context.update({
                "error_message": "Invalid credentials",
                **{key:value[0] for key, value in dict(request.POST).items()},
            })
    return render(request, template_name, context)