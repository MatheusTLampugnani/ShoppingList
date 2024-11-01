from django import forms
from .models import listaCompra, itensLista

class ListaForm(forms.ModelForm):
    class Meta:
        model = listaCompra
        fields = ['nome_lista']
        labels = {'nome_lista': 'Nome da Lista'}

class ItemForm(forms.ModelForm):
    class Meta:
        model = itensLista
        fields = ['nome_item', 'quantidade', 'unidade']
        labels = {
            'nome_item': 'Item da Lista',
            'quantidade': 'Quantidade',
            'unidade': 'Unidade'
        }
        widgets = {
            'unidade': forms.Select(choices=[('kg', 'kg'), ('und', 'und')]),
        }
