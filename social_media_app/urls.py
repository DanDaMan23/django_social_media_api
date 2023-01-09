from django.urls import path, include

from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from social_media_app import views

router = routers.DefaultRouter()
router.register(r'user', views.UserViewSet)
router.register(r'group', views.GroupViewSet, basename='groups')
router.register(r'posts', views.PostViewSet, basename='posts')

# router.register(r'post', views.post_list)

# Wire up our API using automatic URL routing.
# Additionaly, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('register/', views.RegisterUserView.as_view()),
    path('api-token-auth/', obtain_auth_token)
]
