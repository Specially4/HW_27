from datetime import date

from rest_framework import serializers


class NotInDomainValidator:
    def __init__(self, domains: str | list, message: str):
        if not isinstance(domains, list):
            domains = [domains]

        self.domains = domains
        self.message = message

    def __call__(self, value):
        if value.split('@')[-1] in self.domains:
            raise serializers.ValidationError(self.message)


class AgeValidator:
    def __init__(self, limit_value: int, message: str):
        self.message = message
        self.limit_value = limit_value

    def __call__(self, value):
        age = (date.today() - value).days // 365
        if age < self.limit_value:
            raise serializers.ValidationError(self.message)
