from django.shortcuts import redirect, render, get_object_or_404
from .models import *
from .articleform import ArticleForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.
def home__view(request):
    # articles = Article.objects.all()
    return render(request, "index.html")


def about__view(request):
    return render(request, "about.html")


def custom_404(request, exception):
    return render(request, "404.html")


def contact__view(request):
    return render(request, "contact.html")


@login_required
def articles__view(request):
    articles = Article.objects.all()
    return render(request, "articles.html", {"articles": articles})


@login_required(login_url="account:login")
def addarticle__view(request):
    form = ArticleForm(request.POST or None)
    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()

        messages.success(request, "Successfully Added Your Article")
        return redirect("dashboard")

    context = {"form": form}
    return render(request, "addarticle.html", context)


@login_required(login_url="account:login")
def dashboard__view(request):
    articles = Article.objects.filter(author=request.user)
    return render(request, "dashboard.html", {"articles": articles})


@login_required(login_url="account:login")
def article__detail__view(request, id):
    # def article__detail__view(request, id):

    ##article = Article.objects.get(id=id)
    # context = {"article": article}
    # return render(request, "article-detail.html", context)
    # article = Article.objects.filter(slug=slug).first()

    # article = Article.objects.filter(id=id).first()
    article = get_object_or_404(Article, id=id)
    context = {"article": article}
    return render(request, "article-detail.html", context)
