from rest_framework.serializers import ModelSerializer, ReadOnlyField
from rest_framework import status
from social_media_app.models import Post, Comment


class PostSerializer(ModelSerializer):

    class Meta:
        model = Post
        fields = ['id', "content", "user", "comments"]
        read_only_fields = ["comments"]
        user = ReadOnlyField(source='user.url')


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ["content", "post", "user"]
        read_only_fields = ['user']
