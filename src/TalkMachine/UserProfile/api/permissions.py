from rest_framework.permissions import IsAuthenticated

from ..constants import USER_ALREADY_AUTHENTICATED_MSG


class IsNotAuthenticated(IsAuthenticated):

    message = USER_ALREADY_AUTHENTICATED_MSG

    def has_permission(self, request, view):

        not_logged_in = not super(IsNotAuthenticated, self).has_permission(request, view)
        print("NL: ", not_logged_in, request.data, view)
        return not_logged_in
