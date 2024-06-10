from django.db import models


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=150, null=True, blank=True)
    email = models.CharField(max_length=150, null=True, blank=True)
    message = models.TextField(max_length=250, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.name}"
