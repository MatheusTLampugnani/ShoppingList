from django import forms
from django.contrib.auth.models import User
from .models import ShoppingList, Item

class ShoppingListForm(forms.ModelForm):
    """
    Formulário para criar ou editar uma lista de compras.
    """
    class Meta:
        model = ShoppingList
        fields = ['name']  # Campos do modelo que serão incluídos no formulário
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Nome da lista', 'class': 'form-control'}),
        }

class ItemForm(forms.ModelForm):
    """
    Formulário para adicionar ou editar um item na lista de compras.
    """
    class Meta:
        model = Item
        fields = ['name', 'quantity']  # Campos do modelo que serão incluídos no formulário
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Nome do item', 'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'placeholder': 'Quantidade', 'class': 'form-control'}),
        }

