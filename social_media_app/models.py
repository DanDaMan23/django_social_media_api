from django.db import models
from django.contrib.auth.models import User, Group

# Create your models here.


class Post(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, related_name="posts")
