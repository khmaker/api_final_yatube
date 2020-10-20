from django.shortcuts import get_object_or_404
from rest_framework import permissions, viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import (CommentSerializer,
                          PostSerializer,
                          GroupSerializer,
                          FollowSerializer,)
from .permissions import IsOwnerOrReadOnly
from .models import Post, Group, Follow


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['group', ]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        post = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        return post.comments.all()


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsOwnerOrReadOnly]
    http_method_names = ['get', 'post']


class FollowViewSet(viewsets.ModelViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['=user__username', '=following__username']
    http_method_names = ['get', 'post']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
