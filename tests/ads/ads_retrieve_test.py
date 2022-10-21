import pytest

from ads.serializers.serializers_ad import AdRetrieveSerializer


@pytest.mark.django_db
def test_retrieve_ad(client, ad, my_token):
    
    response = client.get(
        f'/ad/{ad.pk}/',
        HTTP_AUTHORIZATION='Bearer ' + my_token
    )

    assert response.status_code == 200
    assert response.data == AdRetrieveSerializer(ad).data
