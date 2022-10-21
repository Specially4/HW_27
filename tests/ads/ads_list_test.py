import pytest

from ads.models import Ad
from users.models import User


@pytest.mark.django_db
def test_ads_list(client, ad, user):
    # user = User.objects.create(
    #     first_name="John",
    #     last_name="Dow",
    #     username="jdow",
    #     password="Qwer1234",
    #     role="moderator",
    #     age=9,
    #     birth_date="2010-10-14",
    #     email="jdow@gmail.com"
    # )
    # ads = Ad.objects.create(
    #     name='Сибирская котята, 3 месяца',
    #     price=2500,
    #     description="Продаю котят",
    #     author_id=user,
    #     is_published=False
    # )

    expected_response = {
        'count': 1,
        'next': None,
        'previous': None,
        'results': [{
            'id': ad.pk,
            'name': '',
            'author_id': ad.author_id.pk,
            'price': 2500,
            'description': None,
            'is_published': False,
            'image': None,
            'category_id': ad.category_id.pk
        }]
    }
    response = client.get('/ad/')

    assert response.status_code == 200
    assert response.data['results'] == expected_response['results']
    