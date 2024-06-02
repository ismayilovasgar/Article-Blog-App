from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify


# Create your models here.
class Article(models.Model):
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    # content = models.TextField()
    content = RichTextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} | {self.author}"


class User(models.Model):
    username = models.TextField(unique=True, max_length=40)
    sluq = models.SlugField(
        blank=True,
        unique=True,
        db_index=True,
        editable=False,
    )

    def save(self, *args, **kwargs):
        self.slug = slugify(self.username)
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.username}"
