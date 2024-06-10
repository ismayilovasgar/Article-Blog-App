from contact.views import *
from django.urls import path

app_name="contact"
urlpatterns = [
    path("", contact__page, name="message"),
    # path("", contact__page2, name="contact"),
]
