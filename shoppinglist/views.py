from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import listaCompra, itensLista
from datetime import datetime

def index(request):
    return render(request, 'lista/index.html')

def criarlista(request):
    return render(request, 'lista/criarlista.html')  # Redireciona para a página de criar lista
