from django.db import models
from django.contrib.auth.models import User


class UserProfileManager(models.Manager):

    use_for_related_fields = True

    def get_user_by_email(self, email):

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise self.model.DoesNotExist

        return user.user_profile

    def get_user_by_username(self, username):

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise self.model.DoesNotExist

        return user.user_profile

    def create(self, email, username, password):
        user = User(
            email=email,
            username=username
        )
        user.set_password(password)
        user.save()

        user_profile = self.model(user=user)
        user_profile.save()

        return user_profile

