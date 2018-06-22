from rest_framework import serializers

from ..models import Contact


class ContactSerializer(serializers.ModelSerializer):

    username = serializers.CharField(
        source='to_user.user.username',
        read_only=True
    )

    first_name = serializers.CharField(
        source='to_user.user.first_name',
        read_only=True
    )

    last_name = serializers.CharField(
        source='to_user.user.last_name',
        read_only=True
    )

    class Meta:
        model = Contact
        fields = (
            'username',
            'first_name',
            'last_name',
        )