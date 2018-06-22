from django.utils.translation import gettext as _


def error_detail_formatter(start, value, end):
    return '{0} {1} {2}'.format(_(start), value, _(end))