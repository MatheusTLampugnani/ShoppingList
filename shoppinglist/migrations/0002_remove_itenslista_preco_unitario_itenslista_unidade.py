# Generated by Django 5.1.2 on 2024-11-01 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoppinglist', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itenslista',
            name='preco_unitario',
        ),
        migrations.AddField(
            model_name='itenslista',
            name='unidade',
            field=models.CharField(choices=[('kg', 'kg'), ('und', 'und')], default='kg', max_length=10),
            preserve_default=False,
        ),
    ]
