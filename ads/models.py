from django.db import models

from users.models import User


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Ad(models.Model):
    IS_PUBLIC = [
        (True, 'Опубликовано'),
        (False, 'Не опубликовано'),
    ]
    name = models.CharField(max_length=255)
    author_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ads')
    price = models.PositiveIntegerField()
    description = models.TextField(null=True)
    is_published = models.BooleanField(choices=IS_PUBLIC, default=False)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    category_id = models.ForeignKey(Category, null=True, on_delete=models.CASCADE, related_name='ads')

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'

    def __str__(self):
        return self.name

    @property
    def username(self):
        return self.author_id.username if self.author_id else None

    @property
    def category(self):
        return self.category_id.name if self.category_id else 'Без категории'
