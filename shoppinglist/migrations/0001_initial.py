# Generated by Django 5.1.2 on 2024-11-05 18:54

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_categoria', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ListaCompra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_lista', models.CharField(max_length=100)),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ItensLista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_item', models.CharField(max_length=100)),
                ('quantidade', models.PositiveIntegerField(default=1)),
                ('unidade_massa', models.CharField(max_length=3)),
                ('comprado', models.BooleanField(default=False)),
                ('categoriaItem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categoria', to='shoppinglist.categoria')),
                ('listaCompra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='shoppinglist.listacompra')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
