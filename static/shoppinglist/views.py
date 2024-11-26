from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .models import ListaCompra, ItensLista
from .forms import ShoppingListForm, ItemForm, UserLoginForm
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
            messages.success(request,'Lista de compras criada com sucesso!')
            return redirect('index')
    else:
        form = ShoppingListForm()
    
    return render(request, 'lista/criar_lista.html', {'form': form})

#funçao detalhes da lista
@login_required
def lista_detalhes(request, lista_id):
    lista = get_object_or_404(ListaCompra, id=lista_id, user=request.user)
    return render(request, 'lista/lista_detalhes.html', {'lista': lista})

#funçao adicionar item
@login_required
def adicionar_item(request, lista_id):
    lista = get_object_or_404(ListaCompra, id=lista_id, user=request.user)

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

#funçao de filtro
@login_required
def lista_filtrada(request):
    if request.method == 'GET':
        # Captura os parâmetros de filtro
        query = request.GET.get('query', '')
        lista_id = request.GET.get('lista_id')
        
        lista = get_object_or_404(ListaCompra, id=lista_id, user=request.user)
        
        # Filtra os itens com base na query
        items = lista.items.filter(name__icontains=query) if query else lista.items.all()

        return render(request, 'lista/lista_filtrada.html', {'lista': lista, 'items': items})

#funçao de marcar como comprado
@login_required
def marcar_item(request, item_id):
    item = get_object_or_404(ItensLista, id=item_id)
    item.purchased = not item.purchased  # Alternar estado de comprado
    item.save()
    messages.success(request, f'Item "{item.nome_item}" {"comprado" if item.comprado else "não comprado"}.')
    return redirect('lista/lista_detalhes', lista_id=item.shopping_list.id)

#funçao de historico
@login_required
def historico_compras(request):
    listas = ListaCompra.objects.filter(user=request.user)
    return render(request, 'lista/historico_compras.html', {'listas': listas})

#funçao de ediçao
@login_required
def editar_item(request, item_id=None):
    item = None
    form = None

    if item_id:
        item = get_object_or_404(ItensLista, id=item_id)
        form = ItemForm(instance=item)
    else:
        form = ItemForm()

    if request.method == 'POST':
        if item_id:
            form = ItemForm(request.POST, instance=item)
            if form.is_valid():
                form.save()
                return redirect('lista/lista_detalhes', lista_id=item.lista.id)
        else:
            item_id = request.POST.get('item_id')
            if item_id:
                return redirect('editar_item_com_id', item_id=item_id)

    context = {
        'items': ItensLista.objects.all(),
        'form': form,
    }

    return render(request, 'lista/editar_item.html', context)

#funçao de reutilizar lista
@login_required
def reutilizar_lista(request, lista_id):
    lista = get_object_or_404(ListaCompra, id=lista_id, user=request.user)
    nova_lista = ListaCompra.objects.create(user=request.user, name=f'Reutilização de {lista.name}')

    for item in lista.items.all():
        ItensLista.objects.create(name=item.name, quantity=item.quantity, shopping_list=nova_lista)

    messages.success(request, 'Lista reutilizada com sucesso!')
    return redirect('lista/index')

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