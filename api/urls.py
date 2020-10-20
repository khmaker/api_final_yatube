from django.urls import include, path
from rest_framework_simplejwt.views import (
        TokenObtainPairView,
        TokenRefreshView,
    )
from rest_framework.routers import DefaultRouter

from . import views


router_v1 = DefaultRouter()
router_v1.register(r'posts',
                   views.PostViewSet,
                   basename='posts')
router_v1.register(r'posts/(?P<post_id>\d+)/comments',
                   views.CommentViewSet,
                   basename='comments')
router_v1.register(r'group',
                   views.GroupViewSet,
                   basename='group')
router_v1.register(r'follow',
                   views.FollowViewSet,
                   basename='follow')

urlpatterns = [
        path('v1/token/', TokenObtainPairView.as_view(),
             name='token_obtain_pair'),
        path('v1/token/refresh/', TokenRefreshView.as_view(),
             name='token_refresh'),
        path('v1/', include(router_v1.urls)),
        ]
