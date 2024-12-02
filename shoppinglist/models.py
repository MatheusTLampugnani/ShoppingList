from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class ListaCompra(models.Model):
    nome_lista = models.CharField(max_length=100)
    data_criacao = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome_lista

class Categoria(models.Model):
    nome_categoria = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nome_categoria}"

class ItensLista(models.Model):
    nome_item = models.CharField(max_length=100)
    quantidade = models.PositiveIntegerField(default=1)
    unidade_massa = models.CharField(max_length=3)
    comprado = models.BooleanField(default=False)
    listaCompra = models.ForeignKey(ListaCompra, related_name='lista', on_delete=models.CASCADE)
    categoriaItem = models.ForeignKey(Categoria, related_name='categoria', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nome_item} (Quantidade: {self.quantidade})"

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()