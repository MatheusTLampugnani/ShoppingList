from django import forms
from django.contrib.auth.models import User
from .models import ListaCompra, ItensLista

class ShoppingListForm(forms.ModelForm):
    class Meta:
        model = ListaCompra
        fields = ['nome_lista']
        widgets = {
            'nome_lista': forms.TextInput(attrs={'placeholder': 'Nome da lista', 'class': 'form-control'}),
        }

class ItemForm(forms.ModelForm):
    class Meta:
        model = ItensLista
        fields = ['nome_item', 'quantidade']
        widgets = {
            'nome_item': forms.TextInput(attrs={'placeholder': 'Nome do item', 'class': 'form-control'}),
            'quantidade': forms.NumberInput(attrs={'placeholder': 'Quantidade', 'class': 'form-control'}),
        }

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label='Senha')
    confir_password = forms.CharField(widget=forms.PasswordInput, label='Confirmação de Senha')

    class Meta:
        model = User
        fields = ['username', 'email', 'confir_password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confir_password = cleaned_data.get('confir_password')

        if password and confir_password and password != confir_password:
            raise forms.ValidationError('As senhas não coincidem.')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user


class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome de usuário'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Senha'}))
