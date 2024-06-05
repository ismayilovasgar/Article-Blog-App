from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.text import slugify
from django.utils.html import strip_tags


# Create your models here.
class Article(models.Model):
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    # content = models.TextField()
    # content = RichTextField()
    image = models.ImageField(upload_to="myIMG", null=True, blank=True, default="1")
    content = RichTextUploadingField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(
        null=True,
        blank=True,
        db_index=True,
        unique=True,
        editable=True,
    )

    def __str__(self):
        return f"{self.title} | {self.author}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    @property
    def article_content_safe(self):
        return strip_tags(self.content)


# Create your models here.


class Comment(models.Model):
    article = models.ForeignKey(
        Article, on_delete=models.CASCADE, related_name="comments"
    )

    comment_author = models.CharField(max_length=50)
    comment_content = models.TextField(max_length=250)
    comment_date = models.DateTimeField(auto_now_add=True)

    @property
    def comment_content_safe(self):
        return strip_tags(self.comment_content)

    def __str__(self) -> str:
        return f"{self.comment_author}"
