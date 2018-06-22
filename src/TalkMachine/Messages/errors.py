from utils.errors.formatters import error_detail_formatter


class MessageDoesNotExist:
    def __init__(self, message_id):
        self.code = 'message_does_not_exist'
        self.detail = error_detail_formatter('Message ', message_id, 'does not exist')