from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.renderers import StaticHTMLRenderer
from rest_framework.decorators import action

from social_media_app.serializers.post_system_serializers import PostSerializer, CommentSerializer
from social_media_app.models import Post, Comment
from social_media_app.permissions import IsOwnerOrReadOnly


# Create your views here.

class PostViewSet(ModelViewSet):
    """
    This viewset automatically provides 'list', 'create', 'retrieve', 'update' and 'destroy' action.
    """
    queryset = Post.objects.all().order_by('-date_created')
    serializer_class = PostSerializer
    permission_classes = [
        IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    @action(detail=True, renderer_classes=[StaticHTMLRenderer])
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all().order_by('-date_created')
    serializer_class = CommentSerializer
    permission_classes = [
        IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly
    ]

    @action(detail=True, renderer_classes=[StaticHTMLRenderer])
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
