from rest_framework import serializers
from django.contrib.auth.models import User, Group
from rest_framework.response import Response
from rest_framework import status
from rest_framework.validators import UniqueValidator
from rest_framework.authentication import TokenAuthentication

from django.contrib.auth.password_validation import validate_password

from social_media_app.models import Post, Comment, Tag


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True, validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'password2', 'email']
        extra_kwargs = {
            'username': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {'password': "Password fields did not match."}
            )
        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ["content", "user"]
        user = serializers.ReadOnlyField(source='user.url')


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["content", "post", "user"]
        read_only_fields = ['user']
