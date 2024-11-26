from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Página inicial
    path('criar-lista/', views.criar_lista, name='lista/criar_lista'),  # Criar nova lista
    path('lista/<int:lista_id>/', views.lista_detalhes, name='lista/lista_detalhes'),  # Detalhes da lista
    path('lista/<int:lista_id>/adicionar-item/', views.adicionar_item, name='lista/adicionar_item'),  # Adicionar item
    path('lista-filtrada/', views.lista_filtrada, name='lista/lista_filtrada'),  # Listar itens filtrados
    path('marcar-item/<int:item_id>/', views.marcar_item, name='lista/marcar_item'),  # Marcar item como comprado
    path('historico-compras/', views.historico_compras, name='lista/historico_compras'),  # Histórico de compras 
    path('reutilizar-lista/<int:lista_id>/', views.reutilizar_lista, name='lista/reutilizar_lista'),  # Reutilizar lista   
    path('editar_item/', views.editar_item, name='editar_item'), # Editar item
    path('editar-item/<int:item_id>/', views.editar_item, name='lista/editar_item'),  # Editar item
    path('registro/', views.registro, name='lista/registro'),  # Registro de usuário
    path('login/', views.login, name='lista/login'),  # Login de usuário
    path('logout/', views.logout, name='lista/logout'),  # Logout de usuário
]