import factory
import factory.fuzzy

from ads.models import Ad, Category
from users.models import User


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    slug = factory.fuzzy.FuzzyText(length=10)

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
        
    username = factory.Faker('name')
    password = 'password'
    first_name = "John"
    last_name = "Dow"
    role = "admin"
    age = 25
    birth_date = "1997-10-14"
    email = factory.Faker('email')


class AdFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Ad

    price = 2500
    author_id = factory.SubFactory(UserFactory)
    category_id = factory.SubFactory(CategoryFactory)
