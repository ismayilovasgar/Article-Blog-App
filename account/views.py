from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import *


# Create your views here.
def register__view(request):
    form = RegisterForm(request.POST or None)

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        newUser = User(username=username)
        newUser.set_password(password)
        newUser.save()

        login(request, newUser)
        messages.success(request, "Ugurla qeydiyyatdan kecdiniz...")

        return redirect("home")

    messages.warning(request, "Qeydiyyatda ugursuz bas verdi...")
    context = {"form": form}
    # return render(request, "register.html", context)
    return render(request, "register.html", context)


def login__view(request):
    form = LoginForm(request.POST or None)
    context = {"form": form}

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username=username, password=password)

        if user is None:

            return render(request, "login.html")

        login(request, user)
        messages.success(request, "Ugurla giris etdiniz...")

        return redirect("home")

    # return render(request, "login.html", context)
    messages.warning(request, "Girisde ugursuz bas verdi...")
    return render(request, "login.html", context)


def logout__view(request):
    logout(request)
    return redirect("home")
