from django.shortcuts import redirect, render
from .forms import *


# Create your views here.
def register__view(request):
    form = RegisterForm(request.POST or None)

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
    context = {"form": form}
    return render(request, "register.html", context)


def login__view(request):
    return render(request, "login.html")


def logout__view(request):
    # return redirect("home")
    # return render(request, "login.html")
    pass
