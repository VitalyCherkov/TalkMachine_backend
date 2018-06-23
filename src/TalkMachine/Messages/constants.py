from django.utils.translation import gettext as _

ACCESS_DENIED = _('Access denied')
# If trying to reply to the message which ID >= of current
MESSAGING_CHRONOLOGY_CONFLICT = _('Messaging chronology conflict')

ROOT_MESSAGE_ID = 0

SENT = 'S'
DELIVERED = 'D'
READ = 'R'

STATUS_CHOICES = (
    (SENT, _('Sent')),
    (DELIVERED, _('Delivered')),
    (READ, _('Read'))
)
