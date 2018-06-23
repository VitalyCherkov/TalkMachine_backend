from django.urls import path

from .api.viewsets import MessageViewSet, ConversationViewSet


message_to_username = MessageViewSet.as_view({'post': 'create'})
message_edit = MessageViewSet.as_view({'post': 'update'})
message_delete = MessageViewSet.as_view({'post': 'destroy'})
message_detail = MessageViewSet.as_view({'get': 'retrieve'})
messages_list = MessageViewSet.as_view({'get': 'list'})

conversations_list = ConversationViewSet.as_view({'get': 'list'})
conversation_detail = ConversationViewSet.as_view({'get': 'retrieve'})

urlpatterns = [
    path(
        'to/<username>',
        message_to_username,
        name='message-to-username'
    ),
    path(
        '<id>/edit',
        message_edit,
        name='message-edit'
    ),
    path(
        '<id>/delete',
        message_delete,
        name='message-delete'
    ),
    path(
        '<id>',
        message_detail,
        name='message-detail'
    ),
    path(
        'conversation/<conversation_id>/page/<page>',
        messages_list,
        name='messages-list'
    ),
    path(
        'conversations/page/<page>',
        conversations_list,
        name='conversations-list'
    ),
    path(
        'conversation/<conversation_id>',
        conversation_detail,
        name='conversation-detail'
    )
]
