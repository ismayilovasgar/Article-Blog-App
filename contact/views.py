from django.shortcuts import render
from .models import Contact
from django.contrib import messages


# Create your views here.
def contact__page(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        result = Contact(
            name=name,
            email=email,
            message=message,
        )
        result.save()
        messages.success(request, "Müraciətiniz uğurla göndərildi...")

    return render(request, "contact.html")
