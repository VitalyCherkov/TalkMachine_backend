from django.http import QueryDict

from rest_framework import viewsets, authentication, status, response
from rest_framework.permissions import IsAuthenticated

from UserProfile.models import UserProfile

from ..models import Message, Conversation

from .permissions import IsOwnMessage
from .serializers import (
    MessageCreateSerializer,
    MessageUpdateSerializer,
    MessageDetailSerializer,
    MessageShortSerializer,
)


class MessageViewSet(viewsets.ModelViewSet):

    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = [IsAuthenticated]
    lookup_url_kwarg = 'id'

    def get_permissions(self):
        permissions = super(MessageViewSet, self).get_permissions()
        if self.action == 'update' or self.action == 'destroy':
            permissions += [IsOwnMessage()]

    def get_queryset(self):

        if 'conversation_id' in self.kwargs:
            return Message.objects.get_not_deleted_queryset()
        else:
            return Message.objects.get_not_deleted_from_conversation(
                conversation_id=self.kwargs['conversation_id'])

    def create(self, request, *args, **kwargs):
        data = request.data
        data += kwargs
        serializer = MessageCreateSerializer(
            data=data,
            context=request.user.user_profile
        )

        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(
            status=status.HTTP_201_CREATED,
            data=serializer.data
        )

    def update(self, request, *args, **kwargs):
        kwargs += {'partial': True}
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

    # TODO: Сделать, наверное, mixin, т.к. это копипаст
    def paginate_queryset(self, queryset):
        # Номер страницы берется пагинатором из поля 'page' в query_params.
        # Поэтому он туда явно записыватся из параметров пути
        self.serializer_class = MessageShortSerializer
        query_params = QueryDict.copy(self.request.query_params)
        query_params.update({'page': self.kwargs['page']})
        return self.paginator.paginate_queryset(queryset, self.request, view=self)


class ConversationViewSet(viewsets.ModelViewSet):

    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = [IsAuthenticated]
    lookup_url_kwarg = 'id'

    def get_queryset(self):
        return Conversation.objects.get_conversations_by_user_profile(
            self.request.user.user_profile)

    # TODO: Сделать, наверное, mixin, т.к. это копипаст
    def paginate_queryset(self, queryset):
        # Номер страницы берется пагинатором из поля 'page' в query_params.
        # Поэтому он туда явно записыватся из параметров пути
        self.serializer_class = MessageShortSerializer
        query_params = QueryDict.copy(self.request.query_params)
        query_params.update({'page': self.kwargs['page']})
        return self.paginator.paginate_queryset(queryset, self.request, view=self)






