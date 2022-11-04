from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import PostViewSet, GroupViewSet, CommentViewSet, FollowViewSet


router_v1 = DefaultRouter()
router_v1.register(r'posts', PostViewSet, 'posts')
router_v1.register(r'groups', GroupViewSet, 'groups')
router_v1.register(r'posts/(?P<id>\d+)/comments', CommentViewSet, 'comments')
router_v1.register(r'follow', FollowViewSet, 'follow')

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/', include('djoser.urls.jwt')),
]
