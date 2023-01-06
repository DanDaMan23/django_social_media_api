from django.contrib.auth.models import User, Group
from rest_framework import serializers
from social_media_app.models import Post


class UserSerializer(serializers.HyperlinkedModelSerializer):
    posts = serializers.HyperlinkedRelatedField(
        many=True, view_name='post-detail', read_only=True)

    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups', 'password', 'posts']
        extra_kwargs = {
            'password': {'write_only': True}
        }


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class PostSerializer(serializers.ModelSerializer):
    # content = serializers.HyperlinkedIdentityField(view_name='post-content')

    class Meta:
        model = Post
        fields = "__all__"
        user = serializers.ReadOnlyField(source='user.url')
