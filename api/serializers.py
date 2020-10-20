from django.contrib.auth.models import User
from rest_framework.serializers import (
    CurrentUserDefault, ModelSerializer, SlugRelatedField,
    )
from rest_framework.validators import UniqueTogetherValidator

from .models import Comment, Follow, Group, Post


class PostSerializer(ModelSerializer):
    author = SlugRelatedField(read_only=True, slug_field='username')

    class Meta:
        fields = '__all__'
        model = Post


class CommentSerializer(ModelSerializer):
    author = SlugRelatedField(read_only=True, slug_field='username')

    class Meta:
        fields = '__all__'
        model = Comment


class GroupSerializer(ModelSerializer):
    class Meta:
        fields = ('id', 'title',)
        model = Group


class FollowSerializer(ModelSerializer):
    user = SlugRelatedField(read_only=True,
                            slug_field='username',
                            default=CurrentUserDefault())
    following = SlugRelatedField(slug_field='username',
                                 queryset=User.objects.all())

    class Meta:
        fields = ('user', 'following')
        model = Follow
        validators = [
                UniqueTogetherValidator(
                        queryset=Follow.objects.all(),
                        fields=['user', 'following']
                        )
                ]
