from django.db import models
from datetime import datetime

class itensLista(models.Model):
    nome_item = models.CharField(max_length=200)
    quantidade = models.IntegerField()
    preco_unitario = models.FloatField()
    def __str__(self):
        return self.nome_item
    
class listaCompra(models.Model):
    nome_lista = models.CharField(max_length=200)
    data_criacap = models.DateField()
    def __str__(self):
        return self.nome_lista
    
class Categoria(models.Model):
    nome_categoria = models.CharField(max_length=200)
    def __str__(self):
        return self.nome_categoria
