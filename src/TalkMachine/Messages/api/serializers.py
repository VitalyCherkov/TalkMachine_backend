from rest_framework import serializers, exceptions
from ..models import Message

from UserProfile.models import UserProfile
from UserProfile.errors import UserDoesNotExists
from UserProfile.api.serializers import UserShortSerializer

from ..constants import ROOT_MESSAGE_ID, MESSAGING_CHRONOLOGY_CONFLICT
from ..errors import MessageDoesNotExist


class MessageCreateSerializer(serializers.ModelSerializer):

    created = serializers.DateTimeField(read_only=True)
    # TODO: parent_msg_serializer
    username = serializers.CharField(write_only=True)
    parent_msg_id = serializers.IntegerField(write_only=True, required=False)
    text = serializers.CharField(required=True)

    class Meta:
        model = Message
        fields = (
            'created',
            'username',
            'parent_msg_id',
            'text'
        )

    def validate_parent_msg_id(self, value):
        if value is None or value == ROOT_MESSAGE_ID:
            return value

        try:
            parent_msg = self.Meta.model.objects.get_not_deleted(message_id=value)
        except self.Meta.model.DoesNotExist:
            error = MessageDoesNotExist(value)
            raise exceptions.ValidationError(detail=error.detail, code=error.code)

        # Грязненько ...
        self.context['parent_msg_id'] = \
            parent_msg.id if parent_msg else 0
        return value

    def validate_username(self, value):
        try:
            user_profile = UserProfile.objects.get_user_by_username(value)
        except UserProfile.DoesNotExist:
            error = UserDoesNotExists(value)
            raise exceptions.ValidationError(detail=error.detail, code=error.code)

        # Грязненько ...
        self.context['to_user_profile'] = user_profile
        return value

    def create(self, validated_data):
        message = self.Meta.model.objects.write_to_conversation(
            text=validated_data['text'],
            from_user_profile=self.context.get('user_profile'),
            to_user_profile=self.context.get('to_user_profile'),
            parent_msg_id=self.context.get('parent_msg_id', 0)
        )
        message.save()
        return message


class MessageUpdateSerializer(serializers.ModelSerializer):

    # TODO: parent_msg_serializer
    parent_msg_id = serializers.IntegerField(required=False)
    text = serializers.CharField(required=False)
    is_edited = serializers.BooleanField(read_only=True)

    # TODO: Убрать копипаст!
    def validate_parent_msg_id(self, value):
        if value is None or value == ROOT_MESSAGE_ID:
            return value

        try:
            parent_msg = self.Meta.model.objects.get_not_deleted(message_id=value)
        except self.Meta.model.DoesNotExist:
            error = MessageDoesNotExist(value)
            raise exceptions.ValidationError(detail=error.detail, code=error.code)

        if not parent_msg.can_be_replied_to_this(self.instance):
            raise exceptions.ValidationError(MESSAGING_CHRONOLOGY_CONFLICT)

        self.context['parent_msg'] = parent_msg
        return value

    class Meta:
        model = Message
        fields = (
            'created',
            'parent_msg_id',
            'text',
            'is_edited'
        )

    def update(self, instance, validated_data):

        new_text = validated_data.get('text', instance.text)
        new_parent_msg_id = validated_data.get('parent_msg_id', instance.parent_msg_id)

        if new_parent_msg_id != instance.parent_msg_id or new_text != instance.text:
            instance.is_edited = True

        instance.text = new_text
        instance.parent_msg_id = new_parent_msg_id
        instance.save()
        return instance


class MessageDetailSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(read_only=True)
    text = serializers.CharField(read_only=True)
    created = serializers.DateTimeField(read_only=True)
    is_edited = serializers.BooleanField(read_only=True)
    parent_msg_id = serializers.IntegerField(read_only=True)
    conversation_id = serializers.IntegerField(read_only=True, source='conversation.id')
    author = UserShortSerializer(read_only=True)

    class Meta:
        model = Message
        fields = (
            'id',
            'text',
            'created',
            'is_edited',
            'parent_msg_id',
            'conversation_id',
            'author',
            # TODO:
            # 'chat_id',
            # 'votes',
            # 'voted',
        )

class MessageShortSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message