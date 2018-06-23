from rest_framework import permissions

from ..constants import ACCESS_DENIED


class IsOwnMessage(permissions.BasePermission):

    message = ACCESS_DENIED

    def has_object_permission(self, request, view, obj):
        return request.user.user_profile == obj.author


class IsOwnConversation(permissions.BasePermission):

    message = ACCESS_DENIED

    def has_object_permission(self, request, view, obj):
        raise NotImplemented('IsOwnConversation')
