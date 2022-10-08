from rest_framework import serializers

from ads.models import Ad


class AdListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ['id', 'name', 'username', 'price', 'category']


class AdDetailSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    category = serializers.CharField()

    class Meta:
        model = Ad
        exclude = ('author_id', 'category_id')


class AdCreateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Ad
        fields = '__all__'

    def is_valid(self, *, raise_exception=False):
        try:
            self._image = self.initial_data.pop('image')
        except:
            self._image = None
        return super().is_valid(raise_exception=raise_exception)


class AdUpdateSerializer(serializers.ModelSerializer):
    author_id = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Ad
        fields = [
            'id',
            'name',
            'author_id',
            'price',
            'description',
            'is_published',
            'image',
            'category_id'
        ]

    def is_valid(self, *, raise_exception=False):
        try:
            self._image = self.initial_data.pop('image')
        except:
            self._image = None
        return super().is_valid(raise_exception=raise_exception)


class AdDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ['id']
