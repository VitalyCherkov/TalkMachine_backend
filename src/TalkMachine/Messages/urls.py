from django.urls import path

from .api.viewsets import MessageViewSet, ConversationViewSet


message_to_username = MessageViewSet.as_view({'post': 'create'})
message_edit = MessageViewSet.as_view({'post': 'update'})
message_delete = MessageViewSet.as_view({'post': 'destroy'})

urlpatterns = [
    path('to/<username>', message_to_username, name='message-to-username'),
    path('<id>/edit', message_edit, name='message-edit'),
    path('<id>/delete', message_delete, name='message-delete'),
]
