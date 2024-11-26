import pytest
from django.urls import reverse

@pytest.mark.django_db
def test_lista_items_view(client):
    url = reverse('shoppinglist:lista_items')
    response = client.get(url)
    assert response.status_code == 200
    assert 'Lista de Itens' in response.content.decode()
