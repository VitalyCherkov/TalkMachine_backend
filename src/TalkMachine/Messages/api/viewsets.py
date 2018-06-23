from django.http import QueryDict

from rest_framework import viewsets, authentication, status, response
from rest_framework.permissions import IsAuthenticated

from UserProfile.models import UserProfile

from ..models import Message, Conversation

from utils.paginators import PathPaginateableViewSetMixin

from .permissions import IsOwnMessage
from .serializers import (
    MessageCreateSerializer,
    MessageUpdateSerializer,
    MessageDetailSerializer,
    MessageShortSerializer,
)


class IsAuthenticatedTest(IsAuthenticated):
    def has_permission(self, request, view):
        res = super(IsAuthenticatedTest, self).has_permission(request, view)
        print(res)
        return res


class MessageViewSet(PathPaginateableViewSetMixin, viewsets.ModelViewSet):

    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = [IsAuthenticatedTest]
    lookup_url_kwarg = 'id'

    def get_permissions(self):
        permissions = super(MessageViewSet, self).get_permissions()
        own_actions = ['update', 'destroy', 'retrieve']
        if self.action in own_actions:
            permissions += [IsOwnMessage()]
        return permissions

    def get_queryset(self):

        if 'conversation_id' not in self.kwargs:
            return Message.objects.get_not_deleted_queryset()
        else:
            return Message.objects.get_not_deleted_from_conversation(
                conversation_id=self.kwargs['conversation_id'])

    def create(self, request, *args, **kwargs):
        data = request.data
        data.update(kwargs)
        serializer = MessageCreateSerializer(
            data=data,
            context={'user_profile': request.user.user_profile}
        )

        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(
            status=status.HTTP_201_CREATED,
            data=serializer.data
        )

    def update(self, request, *args, **kwargs):
        kwargs.update({'partial': True})
        self.serializer_class = MessageUpdateSerializer
        return super(MessageViewSet, self).update(request, args, kwargs)

    def perform_destroy(self, instance):
        instance.set_is_deleted()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.is_deleted:
            return response.Response(status=status.HTTP_404_NOT_FOUND)
        serializer = MessageDetailSerializer(instance)
        return response.Response(serializer.data)


class ConversationViewSet(PathPaginateableViewSetMixin, viewsets.ModelViewSet):

    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = [IsAuthenticated]
    lookup_url_kwarg = 'id'

    def get_queryset(self):
        return Conversation.objects.get_conversations_by_user_profile(
            self.request.user.user_profile)





