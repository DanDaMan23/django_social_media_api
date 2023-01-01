from django.db import models
from django.contrib.auth.models import User, Group

from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight

# Create your models here.


class Post(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, related_name="posts")

    # def save(self, *args, **kwargs):
    #     """
    #     Use the `pygments` library to create a highlighted HTML
    #     representation of the code snippet.
    #     """
    #     lexer = get_lexer_by_name(self.language)  # type: ignore
    #     linenos = 'table' if self.linenos else False  # type: ignore
    #     options = {'title': self.title} if self.title else {}  # type: ignore
    #     formatter = HtmlFormatter(style=self.style, linenos=linenos,  # type: ignore
    #                             full=True, **options)
    #     self.highlighted = highlight(self.code, lexer, formatter)  # type: ignore
    #     super().save(*args, **kwargs)
