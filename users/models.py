from random import choices

from django.db import models


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


class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    role = models.CharField(choices=UserRoles.choices, default='member', max_length=13)
    age = models.PositiveIntegerField(null=True, blank=True)
    location = models.ManyToManyField(Location)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['username']

    def __str__(self):
        return f'Пользователь {self.first_name} {self.last_name}'
