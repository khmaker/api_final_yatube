# coding=utf-8
from django.contrib.auth import get_user_model
from django.db.models import (
    CASCADE, CharField, DateTimeField, ForeignKey, Model,
    SET_NULL, TextField, UniqueConstraint,
)

User = get_user_model()


class Post(Model):
    text = TextField()
    pub_date = DateTimeField(
        auto_now_add=True,
        db_index=True,
    )
    author = ForeignKey(
        User,
        on_delete=CASCADE,
        related_name='posts',
    )
    group = ForeignKey(
        'Group',
        on_delete=SET_NULL,
        blank=True,
        null=True,
        related_name='posts',
    )


class Group(Model):
    title = CharField(max_length=200)
    description = TextField()


class Comment(Model):
    created = DateTimeField(
        auto_now_add=True,
        db_index=True
    )
    author = ForeignKey(
        User,
        on_delete=CASCADE,
        related_name='comments',
    )
    post = ForeignKey(
        'Post',
        on_delete=CASCADE,
        related_name='comments',
        null=False,
    )
    text = TextField(blank=True)


class Follow(Model):
    user = ForeignKey(
        User,
        on_delete=CASCADE,
        related_name='follower',
    )
    following = ForeignKey(
        User,
        on_delete=CASCADE,
        related_name='following',
    )

    class Meta:
        constraints = (
            UniqueConstraint(
                fields=('user', 'following',),
                name='unique_following'
            ),
        )
