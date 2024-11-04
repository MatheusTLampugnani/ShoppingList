from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Página inicial
    path('criar-lista/', views.criar_lista, name='lista/criar_lista'),  # Criar nova lista
    path('lista/<int:lista_id>/', views.lista_detalhes, name='lista/lista_detalhes'),  # Detalhes da lista
    path('lista/<int:lista_id>/adicionar-item/', views.adicionar_item, name='lista/adicionar_item'),  # Adicionar item
    path('registro/', views.registro, name='lista/registro'),  # Registro de usuário
    path('login/', views.user_login, name='lista/login'),  # Login de usuário
    path('logout/', views.user_logout, name='lista/logout'),  # Logout de usuário
]