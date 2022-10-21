import pytest


@pytest.mark.django_db
def test_create_ad(client, my_token, ad):
    expected_response = {
        'id': ad.pk+1,
        'name': 'Сибирская котята, 3 месяца',
        'author_id': ad.author_id.pk,
        'price': 2500,
        'description': 'Продаю котят',
        'is_published': False,
        'image': None,
        'category_id': None
    }

    data = {
        'name': 'Сибирская котята, 3 месяца',
        'author_id': ad.author_id.pk,
        'price': 2500,
        'description': 'Продаю котят',
        'is_published': False,
    }

    response = client.post(
        '/ad/create/',
        data,
        content_type='application/json',
        HTTP_AUTHORIZATION='Bearer ' + my_token
    )

    assert response.status_code == 201
    assert response.data == expected_response
