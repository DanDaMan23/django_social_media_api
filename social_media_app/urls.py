from django.urls import path, include
from rest_framework import routers
from social_media_app import views

router = routers.DefaultRouter()
router.register(r'user', views.UserViewSet)
router.register(r'group', views.GroupViewSet)
# router.register(r'post', views.post_list)

# Wire up our API using automatic URL routing.
# Additionaly, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('posts/', views.post_list),  # type: ignore
    path('posts/<int:pk>', views.post_detail),  # type: ignore
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
