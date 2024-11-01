# models.py

from django.db import models
from datetime import datetime

class itensLista(models.Model):
    nome_item = models.CharField(max_length=200)
    quantidade = models.IntegerField()
    unidade = models.CharField(max_length=10, choices=[('kg', 'kg'), ('und', 'und')])

    def __str__(self):
        return f"{self.nome_item} - {self.quantidade} {self.unidade}"

class listaCompra(models.Model):
    nome_lista = models.CharField(max_length=200)
    data_criacao = models.DateField(default=datetime.now)  # Adiciona a data de criação automaticamente

    def __str__(self):
        return self.nome_lista

class categoria(models.Model):
    nome_categoria = models.CharField(max_length=200)

    def __str__(self):
        return self.nome_categoria
