from django.contrib.auth.models import User, Group

from rest_framework import viewsets, permissions, mixins, generics, renderers
from rest_framework.decorators import action

from social_media_app.serializers.user_system_serializers import UserSerializer, RegisterSerializer, GroupSerializer
from social_media_app.serializers.post_system_serializers import PostSerializer, CommentSerializer

from social_media_app.models import Post, Comment
from social_media_app.permissions import IsOwnerOrReadOnly


# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    """
    API end point that allows users to be viewed or edited
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class RegisterUserView(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = RegisterSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows group ot be viewed or edited
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class PostViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides 'list', 'create', 'retrieve', 'update' and 'destroy' action.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly
    ]

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
