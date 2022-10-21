import pytest

@pytest.mark.django_db
def test_selection_create(client, my_token, user, ad):
    response = client.post(
        '/selection/create/',
        {
            'name': 'new selection',
            'owner': user.pk,
            'items': [ad.pk]
        },
        content_type='application/json',
        HTTP_AUTHORIZATION='Bearer ' + my_token
    )

    assert response.status_code == 201
    assert response.data == {
        'id': 1,
        'name': 'new selection',
        'owner': user.pk,
        'items': [ad.pk]
}