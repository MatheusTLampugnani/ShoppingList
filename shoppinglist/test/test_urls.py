import pytest
from django.urls import reverse

def test_urls():
    url = reverse('shoppinglist:lista_items')
    assert url == '/lista/itens/'

    url_item_create = reverse('shoppinglist:item_create')
    assert url_item_create == '/item/criar/'
