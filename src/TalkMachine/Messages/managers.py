import math

from django.db import models

from UserProfile.models import UserProfile


class ConversationsManager(models.Manager):

    def get_conversations_by_user_profile(self, user_profile):
        return (user_profile.conversations1 | user_profile.conversations2)\
            .order_by('-last_msg_date')

    def get_or_create_between(self, from_user_profile, to_user_profile):
        return self.get_or_create(
            user1_id=min(from_user_profile.id, to_user_profile.id),
            user2_id=max(from_user_profile.id, to_user_profile.id)
        )


class MessagesManager(models.Manager):

    def write_to_conversation(self, from_user_profile, to_user_profile, text, parent_msg_id):

        # kek
        from .models import Conversation
        conversation, created = Conversation.objects.get_or_create_between(
            from_user_profile=from_user_profile,
            to_user_profile=to_user_profile
        )

        message = self.model(
            author=from_user_profile,
            conversation=conversation,
            text=text,
            parent_msg_id=parent_msg_id
        )

        message.save()
        message.conversation.last_msg_date = message.created
        message.conversation.last_msg_id = message.id
        conversation.save()

        return message

    def get_not_deleted(self, message_id):
        message = self.get(id=message_id)
        if message.is_deleted:
            raise self.model.DoesNotExist
        return message

    def get_not_deleted_queryset(self):
        return self.get_queryset().filter(is_deleted=False)

    def get_not_deleted_from_conversation(self, conversation_id):
        return self.get_not_deleted_queryset().filter(conversation_id=conversation_id)
