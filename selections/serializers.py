from django.shortcuts import get_object_or_404
from rest_framework import serializers

from ads.models import Ad
from ads.serializers.serializers_ad import AdListSerializer
from selections.models import Selection
from users.models import User


class SelectionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Selection
        fields = ["id", "name"]


class SelectionRetrieveSerializer(serializers.ModelSerializer):
    items = AdListSerializer(many=True)

    class Meta:
        model = Selection
        fields = '__all__'


class SelectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Selection
        fields = '__all__'
