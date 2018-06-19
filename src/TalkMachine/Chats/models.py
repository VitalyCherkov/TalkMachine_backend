from django.db import models

from UserProfile.models import UserProfile

from .constants import MAX_CHAT_NAME_LENGTH, USER_CHAT_STATUS_CHOICES, PARTICIPATING



class Chat(models.Model):

    admin = models.ForeignKey(
        to=UserProfile,
        related_query_name='admin_chats',
        on_delete=models.SET_NULL,
        null=True
    )

    name = models.CharField(max_length=MAX_CHAT_NAME_LENGTH)
    is_deleted = models.BooleanField(default=False)
    last_msg_id = models.PositiveIntegerField(default=0)

    def __str__(self):
        return '[#{0}] {1}'.format(self.pk, self.name)


class UserChat(models.Model):

    user = models.ForeignKey(
        to=UserProfile,
        related_name='chats',
        related_query_name='chats',
        on_delete=models.CASCADE
    )

    chat = models.ForeignKey(
        to=Chat,
        related_name='chat_users',
        related_query_name='chat_users',
        on_delete=models.CASCADE
    )

    inviter = models.ForeignKey(
        to=UserProfile,
        related_name='invited_users',
        related_query_name='invited_users',
        on_delete=models.SET_NULL,
        null=True
    )

    status = models.CharField(
        max_length=1,
        choices=USER_CHAT_STATUS_CHOICES,
        default=PARTICIPATING
    )

    muted = models.BooleanField(default=False)
