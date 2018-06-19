from rest_framework import serializers
from rest_framework.renderers import JSONRenderer


class ErrorModel:
    def __init__(self, code, text, data=None):
        self.c, self.t, self.d = code, text, data

    class __ErrorSerializer__(serializers.Serializer):
        code = serializers.CharField(read_only=True)
        text = serializers.CharField(read_only=True)
        data = serializers.CharField(read_only=True, required=False)

    def get_JSON(self):
        JSONRenderer().render(ErrorModel.__ErrorSerializer__(self).data)
