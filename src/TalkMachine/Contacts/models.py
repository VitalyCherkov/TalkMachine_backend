from django.db import models

from UserProfile.models import UserProfile


class Contact(models.Model):

    owner = models.ForeignKey(
        to=UserProfile,
        on_delete=models.CASCADE,
        related_name='own_contacts',
        related_query_name='own_contacts'
    )

    to_user = models.ForeignKey(
        to=UserProfile,
        on_delete=models.CASCADE,
        related_name='in_contacts_of',
        related_query_name='in_contacts_of'
    )
