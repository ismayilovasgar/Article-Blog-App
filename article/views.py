from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
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
    keyword = request.POST.get("keyword")
    if keyword:
        articles = Article.objects.filter(title__contains=keyword)
    else:
        articles = Article.objects.all()
    return render(request, "articles.html", {"articles": articles})


@login_required(login_url="account:login")
def article__update__view(request, id):
    article = get_object_or_404(Article, id=id)
    form = ArticleForm(request.POST or None, request.FILES or None, instance=article)
    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()

        messages.success(request, "Successfully Update Your Article")
        return redirect("dashboard")

    context = {
        "form": form,
        "article": article,
    }
    return render(request, "update.html", context)


@login_required(login_url="account:login")
def article__delete__view(request, id):
    article = get_object_or_404(Article, id=id)
    article.delete()
    messages.success(request, "Successfullt Delete Article")
    return redirect("dashboard")


@login_required(login_url="account:login")
def addarticle__view(request):
    form = ArticleForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()

        messages.success(request, "Successfully Added Your Article")
        return redirect("dashboard")

    context = {"form": form}
    return render(request, "addarticle.html", context)


# dashboard
@login_required(login_url="account:login")
def dashboard__view(request):
    articles = Article.objects.filter(author=request.user)
    return render(request, "dashboard.html", {"articles": articles})


# My Article View
@login_required(login_url="account:login")
def article__detail__view(request, id):
    # article = Article.objects.get(id=id)
    # article = Article.objects.filter(id=id).first()
    article = get_object_or_404(Article, id=id)
    context = {"article": article}
    return render(request, "article-detail.html", context)


# Comment
@login_required(login_url="account:login")
def add__comment__view(request, id):
    article = get_object_or_404(Article, id=id)

    if request.method == "POST":
        comment_author = request.POST.get("comment_author")
        comment_content = request.POST.get("comment_content")

        newComment = Comment(comment_author, comment_content)
        newComment.article = article
        newComment.save()
        messages.success("Successfulyy, Add  Comment To Article")
    return redirect(reverse("article-detail", kwargs={"id": id}))
