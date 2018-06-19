from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework import authentication
from rest_framework.authtoken.models import Token

from .permissions import IsNotAuthenticated
from .serializers import UserSignupSerializer, UserLoginSerializer


class UserSignupViewSet(viewsets.ModelViewSet):
    authentication_classes = (authentication.TokenAuthentication,)
    serializer_class = UserSignupSerializer

    def get_permissions(self):
        permission_classes = []
        if self.action == 'create' or self.action == 'login':
            permission_classes = [IsNotAuthenticated]

        return [permission() for permission in permission_classes]

    def _authenicate(self, user, json):
        token = Token.objects.create(user=user)
        json['token'] = token.key
        return json

    def perform_create(self, serializer):
        user_profile = serializer.save()
        return self._authenicate(user=user_profile.user, json=serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        json = self.perform_create(serializer)
        return Response(json, status=status.HTTP_201_CREATED)

    def logout(self, request):
        Token.delete(request.user.auth_token)
        return Response(status=status.HTTP_200_OK)

    def login(self, request):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        json = serializer





