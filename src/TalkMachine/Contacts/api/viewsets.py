from django.http import QueryDict

from rest_framework import viewsets
from rest_framework import status
from rest_framework import authentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from UserProfile.models import UserProfile

from ..models import Contact
from .serializers import ContactSerializer


class ContactViewSet(viewsets.ModelViewSet):

    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Contact.objects.get_contacts(
            self.request.user.user_profile)

    def get_serializer_class(self):
        return ContactSerializer

    def destroy(self, request, *args, **kwargs):
        try:
            Contact.objects.exclude_contact(
                owner_user_profile=request.user.user_profile,
                dest_username=kwargs['username']
            )
            return Response(status=status.HTTP_200_OK)
        except UserProfile.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def create(self, request, *args, **kwargs):
        print(request.user)

        try:
            Contact.objects.add_contact(
                owner_user_profile=request.user.user_profile,
                dest_username=kwargs['username']
            )
            return Response(status=status.HTTP_201_CREATED)
        except UserProfile.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def paginate_queryset(self, queryset):
        # Номер страницы берется пагинатором из поля 'page' в query_params.
        # Поэтому он туда явно записыватся из параметров пути
        query_params = QueryDict.copy(self.request.query_params)
        query_params.update({'page': self.kwargs['page']})
        return self.paginator.paginate_queryset(queryset, self.request, view=self)

