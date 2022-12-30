from django.contrib.auth.models import User, Group
from rest_framework import serializers
from social_media_app.models import Post


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


# class PostSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     content = serializers.CharField(required=True)
#     user = serializers.CharField(required=True)

#     def create(self, validated_data):
#         """
#         Create and return a new 'Post' instance, given the validated data.
#         """
#         return Post.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.content = validated_data.get('content', instance.content)
#         return instance


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'content', 'user']
