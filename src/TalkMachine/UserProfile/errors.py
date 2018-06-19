from django.utils.translation import gettext as _


class EmailAlreadyInUse:
    def __init__(self, email):
        self.code = 'email_already_in_use'
        self.detail = '{0} {1} {2}'.format(_('Email '), email, _(' already in use'))


class UsernameAlreadyInUse:
    def __init__(self, username):
        self.code = 'username_already_in_use'
        self.detail = '{0} {1} {2}'.format(_('Username '), username, _(' already in use'))


class RequiredField:
    def __init__(self, field_name):
        self.code = 'required_field'
        self.detail = 'Field {0} is required'.format(field_name)