from django.db import models
from django.contrib.auth.models import User

from UserProfile.models import UserProfile

from .managers import ContactsManager


class Contact(models.Model):

    owner = models.ForeignKey(
        to=UserProfile,
        on_delete=models.CASCADE,
        related_name='owner',
        related_query_name='owner'
    )

    to_user = models.ForeignKey(
        to=UserProfile,
        on_delete=models.CASCADE,
        related_name='contact_users',
        related_query_name='contact_users'
    )

    def get_contact_users(self):
        return self.to_user.contact_users

    def __str__(self):
        return 'User {0} has {1}'\
            .format(self.owner.user.username, self.to_user.user.username)

    objects = ContactsManager()

