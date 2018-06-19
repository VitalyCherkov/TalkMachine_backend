from django.utils.translation import gettext as _

SENT = 'S'
DELIVERED = 'D'
READ = 'R'

STATUS_CHOICES = (
    (SENT, _('Sent')),
    (DELIVERED, _('Delivered')),
    (READ, _('Read'))
)
