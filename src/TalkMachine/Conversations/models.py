from django.db import models

from UserProfile.models import UserProfile

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
