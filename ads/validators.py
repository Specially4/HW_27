from rest_framework import serializers


class IsPublishedValidator:
    def __init__(self, message: str, default_value: bool):
        self.default_value = default_value
        self.message = message

    def __call__(self, value):
        if value == self.default_value:
            raise serializers.ValidationError(self.message)
