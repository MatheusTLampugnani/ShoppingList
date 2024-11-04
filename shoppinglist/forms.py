from django import forms
from django.contrib.auth.models import User
from .models import ShoppingList, Item

class ShoppingListForm(forms.ModelForm):
    """
    Formulário para criar ou editar uma lista de compras.
    """
    class Meta:
        model = ShoppingList
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Nome da lista', 'class': 'form-control'}),
        }

class ItemForm(forms.ModelForm):
    """
    Formulário para adicionar ou editar um item na lista de compras.
    """
    class Meta:
        model = Item
        fields = ['name', 'quantity']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Nome do item', 'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'placeholder': 'Quantidade', 'class': 'form-control'}),
        }

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label='Senha')
    confirm_password = forms.CharField(widget=forms.PasswordInput, label='Confirmação de Senha')

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError('As senhas não coincidem.')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user


class UserLoginForm(forms.Form):
    """
    Formulário para o login do usuário.
    """
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome de usuário'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Senha'}))
