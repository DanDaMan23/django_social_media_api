from django.db.models import Model, CharField, DateTimeField, TextField, ForeignKey, CASCADE, ManyToManyField
from django.contrib.auth.models import User

# Create your models here.


class Tag(Model):
    caption = CharField(max_length=30)


class Post(Model):
    date_created = DateTimeField(auto_now_add=True)
    content = TextField()
    user = ForeignKey(
        User, on_delete=CASCADE, null=True, related_name="posts")
    tags = ManyToManyField(Tag)


class Comment(Model):
    date_created = DateTimeField(auto_now_add=True)
    content = TextField()
    user = ForeignKey(
        User, on_delete=CASCADE, null=True, related_name="comments")
    post = ForeignKey(
        Post, on_delete=CASCADE, null=True, related_name="comments")
