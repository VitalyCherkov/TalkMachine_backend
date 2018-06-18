from django.db import models

from UserProfile.models import UserProfile
from Conversations.models import Conversation
from Chats.models import Chat

from .constants import STATUS_CHOICES, DELIVERED


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
