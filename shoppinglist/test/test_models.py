import pytest
from shoppinglist.models import ItensLista

@pytest.mark.django_db
def test_criar_item():
    item = ItensLista.objects.create(nome="Arroz", quantidade=2)
    assert item.nome_item == "Arroz"
    assert item.quantidade == 2

@pytest.mark.django_db
def test_item_str():
    item = ItensLista.objects.create(nome="Feijão", quantidade=3)
    assert str(item) == "Feijão - 3 unidades"
