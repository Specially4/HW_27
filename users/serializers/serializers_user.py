from rest_framework import serializers

from users.models import Location, User
from users.validators import AgeValidator, NotInDomainValidator


class UserListSerializer(serializers.ModelSerializer):
    location = serializers.SlugRelatedField(
        required=False,
        many=True,
        queryset=Location.objects.all(),
        slug_field='name'
    )

    class Meta:
        model = User
        fields = '__all__'


class UserRetrieveSerializer(serializers.ModelSerializer):
    location = serializers.SlugRelatedField(
        required=False,
        many=True,
        queryset=Location.objects.all(),
        slug_field='name'
    )

    class Meta:
        model = User
        exclude = ['password']


class UserCreateSerializer(serializers.ModelSerializer):
    location = serializers.SlugRelatedField(
        required=False,
        many=True,
        queryset=Location.objects.all(),
        slug_field='name'
    )
    birth_date = serializers.DateField(validators=[AgeValidator(
        message='Allowed age 9 and over',
        limit_value=9
    )])
    email = serializers.EmailField(validators=[NotInDomainValidator(
        domains=['rambler.ru'],
        message='Invalid domain'
    )])

    def is_valid(self, *, raise_exception=False):
        self._location = self.initial_data.pop('location', [])
        return super().is_valid(raise_exception=raise_exception)

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        
        user.set_password(validated_data["password"])
        user.save()

        for loc in self._location:
            location, _ = Location.objects.get_or_create(
                name=loc['name'],
                lat=loc['lat'] if 'lat' in loc else None,
                lng=loc['lng'] if 'lng' in loc else None
                )
            user.location.add(location)

        return user

    class Meta:
        model = User
        fields = '__all__'


class UserUpdateSerializer(serializers.ModelSerializer):
    location = serializers.SlugRelatedField(
        required=False,
        many=True,
        queryset=Location.objects.all(),
        slug_field='name'
    )

    class Meta:
        model = User
        fields = '__all__'

    def is_valid(self, *, raise_exception=False):
        self._location = self.initial_data.pop('location')
        return super().is_valid(raise_exception=raise_exception)

    def save(self, **kwargs):
        user = super().save(**kwargs)
        if self.initial_data['password']:
            user.set_password(self.initial_data['password'])
            user.save()

        for loc in self._location:
            location, _ = Location.objects.get_or_create(
                name=loc['name'],
                lat=loc['lat'] if 'lat' in loc else None,
                lng=loc['lng'] if 'lng' in loc else None
                )
            user.location.add(location)

        return user


class UserDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id']
