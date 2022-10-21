import pytest


@pytest.fixture
@pytest.mark.django_db
def my_token(client, django_user_model):
    username = 'jdow'
    password = 'Qwer1234'

    django_user_model.objects.create_user(
        username=username,
        password=password,
        first_name="John",
        last_name="Dow",
        role="admin",
        age=25,
        birth_date="1997-10-14",
        email="jdow@gmail.com"
    )

    response = client.post(
        '/user/token/',
        {'username': username, 'password': password},
        format='json'
    )

    return response.data['access']
