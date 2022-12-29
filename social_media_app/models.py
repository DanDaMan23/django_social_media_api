from django.db import models
from django.contrib.auth.models import User, Group

# Create your models here.


class Post(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    user = models.CharField(max_length=20, null=False)
