from django.shortcuts import redirect, render
from .models import *
from .articleform import ArticleForm
from django.contrib import messages


# Create your views here.
def home__view(request):
    # articles = Article.objects.all()
    return render(request, "index.html")


def articles__view(request):
    articles = Article.objects.all()
    return render(request, "articles.html", {"articles": articles})


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


def dashboard__view(request):
    articles = Article.objects.filter(author=request.user)
    return render(request, "dashboard.html", {"articles": articles})


def about__view(request):
    return render(request, "about.html")


def article__detail__view(request, slug):
# def article__detail__view(request, id):

    ##article = Article.objects.get(id=id)
    # article = Article.objects.filter(id=id).first()
    # context = {"article": article}
    # return render(request, "article-detail.html", context)

    article = Article.objects.filter(slug=slug).first()
    context = {"article": article}
    return render(request, "article-detail.html", context)


def contact__view(request):
    return render(request, "contact.html")
