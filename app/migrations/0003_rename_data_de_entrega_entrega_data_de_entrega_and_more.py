# Generated by Django 4.2.3 on 2024-04-17 17:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_frutas_options_alter_verduras_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entrega',
            old_name='data_de_Entrega',
            new_name='data_de_entrega',
        ),
        migrations.RenameField(
            model_name='frutas',
            old_name='nome',
            new_name='nome_do_produto',
        ),
        migrations.RenameField(
            model_name='frutas',
            old_name='preco_do_produto',
            new_name='preco_unitario',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='nome_item',
            new_name='nome_do_produto',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='precoUnitario',
            new_name='preco_unitario',
        ),
        migrations.RenameField(
            model_name='pagamento',
            old_name='metodo_de_pagemento',
            new_name='metodo_de_pagamento',
        ),
        migrations.RenameField(
            model_name='pagamento',
            old_name='valorTotal',
            new_name='valor_total',
        ),
        migrations.RenameField(
            model_name='verduras',
            old_name='nome',
            new_name='nome_do_produto',
        ),
        migrations.RenameField(
            model_name='verduras',
            old_name='preco_do_produto',
            new_name='preco_unitario',
        ),
    ]
