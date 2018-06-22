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


class MessagesManager(models.Manager):

    def is_in_current_conversation(self, conversation_id, dest_message_id):
        try:
            message = self.get(id=dest_message_id)
            if message.conversation.id == conversation_id:
                return True
            else:
                return False
        except self.model.DoesNotExist:
            return False

    def write_to_conversation(self, from_user_profile, to_username, text, parent_msg_id):

        conversation, _ = ConversationsManager.get_or_create_between(from_user_profile, to_username)

        if parent_msg_id and parent_msg_id != 0:
            if not self.is_in_current_conversation(conversation.id, parent_msg_id):
                raise self.model.DoesNotExist

        message = self.model(
            author=from_user_profile,
            conversation=conversation,
            text=text,
            parent_msg_id=parent_msg_id
        )
        message.save()

        return message

