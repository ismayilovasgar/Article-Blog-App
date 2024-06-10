from django.core.mail import EmailMessage
from django.shortcuts import render
from .models import Contact
from django.contrib import messages
from django.template.loader import render_to_string


# Create your views here.
def contact__page(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        contact = Contact(
            name=name,
            email=email,
            message=message,
        )
        contact.save()

        Context = {"name": name, "message": message}
        html_message = render_to_string("email.html", Context)

        email_message = EmailMessage(
            subject="Contact form inquiry",
            body=html_message,
            from_email="asgar.ismayilov.21@gmail.com",
            to=[email],
        )
        email_message.content_subtype = "html"
        email_message.send()

        messages.success(request, "Müraciətiniz uğurla göndərildi...")

    return render(request, "contact.html")
