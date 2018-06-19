from django.db import models
from django.contrib.auth.models import User

from .managers import UserProfileManager


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
    bio = models.TextField(blank=True)

    objects = UserProfileManager()

    def __str__(self):
        return '{0} {1}'.format(self.user.username, self.user.email)
