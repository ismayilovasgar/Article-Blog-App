from django.core.mail import EmailMessage
from django.shortcuts import render
from .models import Contact
from django.contrib import messages
from django.template.loader import render_to_string
from .forms import *

#  Trasnlator Page
from django.utils import translation
from django.urls.base import resolve, reverse
from django.urls.exceptions import Resolver404
from urllib.parse import urlparse
from django.http import HttpResponseRedirect
from django.conf import settings


# Create your views here.
def contact__page(request):
    # if request.method == "POST":
    #     name = request.POST.get("name")
    #     email = request.POST.get("email")
    #     message = request.POST.get("message")

    #     contact = Contact(
    #         name=name,
    #         email=email,
    #         message=message,
    #     )
    #     contact.save()

    #     Context = {"name": name, "message": message}
    #     html_message = render_to_string("email.html", Context)

    #     email_message = EmailMessage(
    #         subject="Contact form inquiry",
    #         body=html_message,
    #         from_email="asgar.ismayilov.21@gmail.com",
    #         to=[email],
    #     )
    #     email_message.content_subtype = "html"
    #     email_message.send()

    #     messages.success(request, "Müraciətiniz uğurla göndərildi...")

    # return render(request, "contact.html")

    context = dict()
    url = request.META.get("HTTP_REFERER")

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            result = form.save(commit=False)

            name = request.POST.get("name")
            email = request.POST.get("email")
            message = request.POST.get("message")

            result.save()
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
            return HttpResponseRedirect(url)

    else:
        context["form"] = ContactForm()

    return render(request, "contact.html", context)


def set_language(request, language):
    for lang, _ in settings.LANGUAGES:
        translation.activate(lang)
        try:
            view = resolve(urlparse(request.META.get("HTTP_REFERER")).path)
        except Resolver404:
            view = None
        if view:
            break
    if view:
        translation.activate(language)
        next_url = reverse(view.url_name, args=view.args, kwargs=view.kwargs)
        response = HttpResponseRedirect(next_url)
        response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language)
    else:
        response = HttpResponseRedirect("contact/")
    return response
