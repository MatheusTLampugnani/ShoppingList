from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .models import ShoppingList, Item
from .forms import ShoppingListForm, ItemForm, UserRegistrationForm, UserLoginForm
from django.contrib import messages
from django.contrib.auth.models import User

#funçao index
def index(request):
    return render(request, 'lista/index.html')

#funçao criaçao lista
@login_required
def criar_lista(request):
    if request.method == 'POST':
        form = ShoppingListForm(request.POST)
        if form.is_valid():
            shopping_list = form.save(commit=False)
            shopping_list.user = request.user
            shopping_list.save()
            messages.success(request, 'Lista de compras criada com sucesso!')
            return redirect('index')
    else:
        form = ShoppingListForm()
    
    return render(request, 'lista/criar_lista.html', {'form': form})

#funçao detalhes da lista
@login_required
def lista_detalhes(request, lista_id):
    lista = get_object_or_404(ShoppingList, id=lista_id, user=request.user)
    return render(request, 'lista/lista_detalhes.html', {'lista': lista})

#funçao adicionar item
@login_required
def adicionar_item(request, lista_id):
    lista = get_object_or_404(ShoppingList, id=lista_id, user=request.user)

    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.shopping_list = lista
            item.save()
            messages.success(request, 'Item adicionado com sucesso!')
            return redirect('lista/lista_detalhes', lista_id=lista.id)
    else:
        form = ItemForm()

    return render(request, 'lista/adicionar_item.html', {'form': form, 'lista': lista})

#funçao registro
def registro(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            messages.error(request, 'As senhas não coincidem. Tente novamente.')
            return render(request, 'lista/registro.html')

        try:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            messages.success(request, 'Conta criada com sucesso! Você pode fazer login agora.')
            return redirect('lista/login')
        except Exception as e:
            messages.error(request, f'Erro ao criar conta: {e}')

    return render(request, 'lista/registro.html')

#funçao login
def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Login bem-sucedido!')
                return redirect('index')
            else:
                messages.error(request, 'Nome de usuário ou senha inválidos.')
    else:
        form = UserLoginForm()
    
    return render(request, 'lista/login.html', {'form': form})

#funçao logout
@login_required
def user_logout(request):
    logout(request)
    messages.success(request, 'Você saiu com sucesso!')
    return redirect('lista/login')
