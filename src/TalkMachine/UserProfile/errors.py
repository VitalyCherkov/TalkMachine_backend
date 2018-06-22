from utils.errors.formatters import error_detail_formatter


class EmptyField:
    def __init__(self, field_name):
        self.code = 'empty_field'
        self.detail = error_detail_formatter('Field', field_name, ' can not be empty')


class EmailAlreadyInUse:
    def __init__(self, email):
        self.code = 'email_already_in_use'
        self.detail = error_detail_formatter('Email ', email, ' already in use')


class UsernameAlreadyInUse:
    def __init__(self, username):
        self.code = 'username_already_in_use'
        self.detail = error_detail_formatter('Username ', username, ' already in use')


class RequiredField:
    def __init__(self, field_name):
        self.code = 'required_field'
        self.detail = error_detail_formatter('Field ', field_name, ' is required')


class UserDoesNotExists:
    def __init__(self, username):
        self.code = 'user_does_not_exist'
        self.detail = error_detail_formatter('User ', username, ' does not exist')
