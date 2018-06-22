from django.db import models
from UserProfile.models import UserProfile


class ContactsManager(models.Manager):

    def get_contacts(self, user_profile):
        return self.get_queryset().filter(owner=user_profile).order_by('to_user__user__username')

    def add_contact(self, owner_user_profile, dest_username):
        dest_user = UserProfile.objects.get_user_by_username(dest_username)
        _, created = self.get_or_create(
            owner=owner_user_profile, to_user=dest_user)
        return created

    def exclude_contact(self, owner_user_profile, dest_username):
        try:
            dest_user_profile = UserProfile.objects.get_user_by_username(dest_username)
            contact = self.get(
                owner=owner_user_profile,
                to_user=dest_user_profile
            )
            contact.delete()
            return True

        except Exception:
            return False
