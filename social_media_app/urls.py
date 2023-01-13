from django.urls import path, include

from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from social_media_app.views.post_system_views import PostViewSet, CommentViewSet
from social_media_app.views.user_system_views import UserViewSet, GroupViewSet, RegisterUserView

router = routers.DefaultRouter()
router.register(r'user', UserViewSet)
router.register(r'group', GroupViewSet, basename='groups')
router.register(r'posts', PostViewSet, basename='posts')
router.register(r'comment', CommentViewSet)

# router.register(r'post', post_list)

# Wire up our API using automatic URL routing.
# Additionaly, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('register/', RegisterUserView.as_view()),
    path('api-token-auth/', obtain_auth_token)
]
