from django.shortcuts import render
from .models import *


# Create your views here.
def home__view(request):
    # articles = Article.objects.all()
    return render(request, "index.html")


def articles__view(request):
    articles = Article.objects.all()
    return render(request, "articles.html", {"articles": articles})


def addarticle__view(request):
    return render(request, "addarticle.html")


def dashboard__view(request):
    articles = Article.objects.filter(author=request.user)
    return render(request, "dashboard.html", {"articles": articles})


def about__view(request):
    return render(request, "about.html")


def contact__view(request):
    return render(request, "contact.html")
