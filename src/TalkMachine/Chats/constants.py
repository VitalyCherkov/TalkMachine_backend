from django.utils.translation import gettext as _


MAX_CHAT_NAME_LENGTH = 50

PARTICIPATING = 'P'
LEFT = 'L'
DELETED = 'D'

USER_CHAT_STATUS_CHOICES = (
    (PARTICIPATING, _('Participating')),
    (LEFT, _('Left')),
    (DELETED, _('Deleted'))
)