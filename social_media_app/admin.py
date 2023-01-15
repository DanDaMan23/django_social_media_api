from django.contrib import admin
from social_media_app.models import Post, Comment, Tag

# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Tag)