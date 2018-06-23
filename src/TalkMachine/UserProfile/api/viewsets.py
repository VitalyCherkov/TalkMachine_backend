from rest_framework import viewsets
from rest_framework import status
from rest_framework import authentication
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token

from django.shortcuts import get_object_or_404

from ..models import User

from .permissions import IsNotAuthenticated
from .serializers import (
    UserSignupSerializer,
    UserLoginSerializer,
    UserMeSerializer,
    UserDetailsSerializer,
    UserShortSerializer,
    UserUpdateSerializer,
)


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    authentication_classes = (authentication.TokenAuthentication,)
    serializer_class = UserSignupSerializer

    def get_permissions(self):
        if self.action == 'create' or self.action == 'login':
            permission_classes = [IsNotAuthenticated]
        else:
            permission_classes = [IsAuthenticated]

        return [permission() for permission in permission_classes]

    def _authenicate(self, user, json):
        try:
            token = Token.objects.get(user=user)
            Token.delete(token)
        except Token.DoesNotExist:
            pass

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
        try:
            Token.delete(request.user.auth_token)
        except Exception:
            pass

        return Response(status=status.HTTP_200_OK)

    def login(self, request):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        json = self._authenicate(user=serializer.instance.user, json=serializer.data)
        return Response(json)

    def get_object(self):
        if 'username' in self.kwargs:
            return get_object_or_404(
                self.get_queryset(), username=self.kwargs['username']
            )
        else:
            return self.request.user.user_profile

    def retrieve_me(self, request):
        serializer = UserMeSerializer(instance=self.get_object())
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        obj = self.get_object().user_profile
        serializer_class = UserDetailsSerializer if 'details' in kwargs else UserShortSerializer
        serializer = serializer_class(obj)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()

        serializer = UserUpdateSerializer(
            instance=instance,
            data=request.data,
            partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)







