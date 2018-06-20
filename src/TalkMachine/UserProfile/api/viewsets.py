from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework import authentication
from rest_framework.decorators import action
from rest_framework.authtoken.models import Token

from ..models import User

from .permissions import IsNotAuthenticated
from .serializers import UserSignupSerializer, UserLoginSerializer


class UserSignupViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    authentication_classes = (authentication.TokenAuthentication,)
    serializer_class = UserSignupSerializer

    def get_permissions(self):
        permission_classes = []
        print('action ', self.action)
        if self.action == 'create':
            permission_classes = [IsNotAuthenticated]
        if self.action == 'login':
            permission_classes = [IsNotAuthenticated]

        return [permission() for permission in permission_classes]

    def _authenicate(self, user, json):
        print('USER: ', user)
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

    @action(methods=['post'], detail=True, permission_classes=[IsNotAuthenticated])
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

    @action(methods=['post'], detail=True, permission_classes=[IsNotAuthenticated])
    def login(self, request):
        print('LOGIN')
        print(request.data)

        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        json = self._authenicate(user=serializer.instance.user, json=serializer.data)
        return Response(json)

    def retrieve_me(self, request, *args, **kwargs):
        """
        '/user/me'
        """
        pass






