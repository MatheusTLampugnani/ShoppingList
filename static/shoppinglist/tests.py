from django.test import TestCase
import pytest
from django.urls import reverse
from shoppinglist.models import ItensLista

@pytest.mark.django_db
def test_criar_item():
    item = ItensLista.objects.create(nome="Arroz", quantidade=2)
    assert item.nome_item == "Arroz"
    assert item.quantidade == 2

@pytest.mark.django_db
def test_view_lista_items(client):
    url = reverse('shoppinglist:lista_items')
    response = client.get(url)
    assert response.status_code == 200
