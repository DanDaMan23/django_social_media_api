from rest_framework.serializers import HyperlinkedModelSerializer, ModelField, EmailField, CharField, ValidationError, ModelSerializer
from django.contrib.auth.models import User, Group
from rest_framework import status
from rest_framework.validators import UniqueValidator

from django.contrib.auth.password_validation import validate_password


class UserSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class RegisterSerializer(ModelSerializer):
    email = EmailField(
        required=True, validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = CharField(
        write_only=True, required=True, validators=[validate_password]
    )
    password2 = CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'password2', 'email']
        extra_kwargs = {
            'username': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise ValidationError(
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


class GroupSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
