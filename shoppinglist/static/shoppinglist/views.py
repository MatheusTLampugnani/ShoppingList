from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import itensLista
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):
    return render(request,'lista/index.html')

def criarlista(request):
    return render(request, 'lista/criarlista.html')