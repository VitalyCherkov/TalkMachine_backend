from django.db import models


from UserProfile.models import UserProfile
from Messages.models import Message


class Conversation(models.Model):

    user1 = models.ForeignKey(
        to=UserProfile,
        related_query_name='conversations1',
        on_delete=models.SET_NULL,
        null=True
    )

    user2 = models.ForeignKey(
        to=UserProfile,
        related_query_name='conversations2',
        on_delete=models.SET_NULL,
        null=True
    )

    last_msg_id = models.OneToOneField(
        to=Message,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )

    deleted = models.BooleanField(default=False)
    favourite = models.BooleanField(default=False)

    def __str__(self):
        return '{0} -> {1}'.format(self.user1.user.username, self.user2.user.username)

