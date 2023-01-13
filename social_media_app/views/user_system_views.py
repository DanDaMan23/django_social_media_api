from django.contrib.auth.models import User, Group

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.generics import CreateAPIView

from social_media_app.serializers.user_system_serializers import UserSerializer, RegisterSerializer, GroupSerializer


# Create your views here.


class UserViewSet(ModelViewSet):
    """
    API end point that allows users to be viewed or edited
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class RegisterUserView(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer


class GroupViewSet(ModelViewSet):
    """
    API endpoint that allows group ot be viewed or edited
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticated]