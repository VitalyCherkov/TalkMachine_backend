from django.db import models

from UserProfile.models import UserProfile
from Chats.models import Chat

from .constants import STATUS_CHOICES, DELIVERED
from .managers import ConversationsManager


class Conversation(models.Model):

    user1 = models.ForeignKey(
        to=UserProfile,
        related_name='conversations1',
        related_query_name='conversations1',
        on_delete=models.SET_NULL,
        null=True
    )

    user2 = models.ForeignKey(
        to=UserProfile,
        related_name='conversations2',
        related_query_name='conversations2',
        on_delete=models.SET_NULL,
        null=True
    )

    last_msg_id = models.PositiveIntegerField(default=0)

    deleted = models.BooleanField(default=False)
    favourite = models.BooleanField(default=False)

    objects = ConversationsManager()

    def __str__(self):
        return '{0} -> {1}'.format(self.user1.user.username, self.user2.user.username)


class Message(models.Model):

    conversation = models.ForeignKey(
        to=Conversation,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_query_name='messages'
    )

    chat = models.ForeignKey(
        to=Chat,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_query_name='messages'
    )

    status = models.CharField(
        max_length=1,
        choices=STATUS_CHOICES,
        default=DELIVERED
    )

    author = models.ForeignKey(
        to=UserProfile,
        on_delete=models.SET_NULL,
        null=True,
        related_name='own_messages'
    )

    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    parent_msg_id = models.PositiveIntegerField(default=0)
    is_edited = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return '[#{0}] - {1}'.format(self.pk, self.text)


class Vote(models.Model):

    message = models.ForeignKey(
        to=Message,
        related_query_name='voted_for',
        on_delete=models.CASCADE
    )

    user = models.ForeignKey(
        to=UserProfile,
        related_query_name='voters',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return '{0} voted for [#{1}]'.format(self.user.user.username, self.message_id)

