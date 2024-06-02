from django.contrib import admin
from .models import *


# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = (
        "author",
        "title",
        "content",
        "created_date",
    )
    search_fields = (
        "author",
        "title",
    )
    list_filter = (
        "author",
        "title",
        "created_date",
    )


class Article_WriterAdmin(admin.ModelAdmin):
    list_display = ("username",)
    list_filter = ("username",)
    search_fields = ("username",)


admin.site.register(Article, ArticleAdmin)
admin.site.register(Article_Writer, Article_WriterAdmin)
