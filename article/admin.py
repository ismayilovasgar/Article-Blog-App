from django.contrib import admin
from .models import Article


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


admin.site.register(Article, ArticleAdmin)
