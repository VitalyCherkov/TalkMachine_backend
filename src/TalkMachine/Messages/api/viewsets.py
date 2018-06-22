from rest_framework import viewsets
from rest_framework import authentication
from rest_framework.permissions import IsAuthenticated


class MessageViewSet(viewsets.ModelViewSet):

    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = [IsAuthenticated]

    # def create(self, request, *args, **kwargs):


