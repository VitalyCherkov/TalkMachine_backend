import math

from django.db import models

from UserProfile.models import UserProfile


class ConversationsManager(models.Manager):

    def get_or_create_between(self, from_user_profile, to_username):

        to_user_profile = UserProfile.objects.get_user_by_username(to_username)

        return self.get_or_create(
            user1_id=min(from_user_profile.id, to_user_profile.id),
            user2_id=max(from_user_profile.id, to_user_profile.id)
        )


