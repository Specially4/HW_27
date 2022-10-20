from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator
from django.db import models

from users.validators import NotInDomainValidator, AgeValidator


class Location(models.Model):
    name = models.CharField(max_length=100)
    lat = models.DecimalField(max_digits=10, decimal_places=8, null=True)
    lng = models.DecimalField(max_digits=10, decimal_places=8, null=True)

    class Meta:
        verbose_name = 'Местоположение'
        verbose_name_plural = 'Местоположения'

    def __str__(self):
        return self.name


class UserRoles:
    USER = 'member'
    ADMIN = 'admin'
    MODERATOR = 'moderator'
    choices = (
        (USER, 'Пользователь'),
        (ADMIN, 'Администратор'),
        (MODERATOR, 'Модератор')
    )


class User(AbstractUser):
    role = models.CharField(choices=UserRoles.choices, default='member', max_length=13)
    age = models.PositiveIntegerField(
        null=True,
        blank=True,
        validators=[MinValueValidator(limit_value=9, message='Allowed age 9 and over')]
    )
    birth_date = models.DateField(validators=[AgeValidator(
        message='Allowed age 9 and over',
        limit_value=9
    )])
    email = models.EmailField(unique=True, validators=[NotInDomainValidator(
        domains=['rambler.ru'],
        message='Invalid domain'
    )])
    location = models.ManyToManyField(Location)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['username']

    def __str__(self):
        return self.username
