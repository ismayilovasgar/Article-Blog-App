from django.contrib import admin
from .models import Article, Comment


# Register your models here.
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["author", "title", "article_content_safe"]
    list_display_links = ["title", "author"]
    search_fields = ["author", "title"]
    list_filter = ["author", "title", "created_date"]

    class Meta:
        model = Article


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["comment_author", "comment_content_safe"]
    list_display_links = ["comment_author"]
    search_fields = ["comment_author", "comment_content"]
    list_filter = ["comment_date", "comment_author"]

    class Meta:
        model = Comment




# old way
# admin.site.register(Article, ArticleAdmin)
# admin.site.register(Comment, CommentAdmin)
# admin.site.register(Contact, ContactAdmin)
