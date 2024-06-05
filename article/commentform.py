from django import forms
from .models import *


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["article", "comment_author", "comment_content", "comment_date"]
