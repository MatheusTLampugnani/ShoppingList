import pytest
from shoppinglist.forms import ItemForm
from shoppinglist.models import ItensLista

@pytest.mark.django_db
def test_formulario_valido():
    form_data = {'nome': 'Maçã', 'quantidade': 5}
    form = ItemForm(data=form_data)
    assert form.is_valid()

@pytest.mark.django_db
def test_formulario_invalido():
    form_data = {'nome': '', 'quantidade': 5}
    form = ItemForm(data=form_data)
    assert not form.is_valid()
    assert 'This field is required' in str(form.errors)
