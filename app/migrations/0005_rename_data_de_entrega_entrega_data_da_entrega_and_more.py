# Generated by Django 4.2.3 on 2024-04-17 23:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_rename_preco_unitario_frutas_preco_individual_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entrega',
            old_name='data_de_entrega',
            new_name='data_da_entrega',
        ),
        migrations.RenameField(
            model_name='entrega',
            old_name='endereco_de_entrega',
            new_name='endereco_da_entrega',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='preco_unitario',
            new_name='preco_individual',
        ),
        migrations.RenameField(
            model_name='pagamento',
            old_name='metodo_de_pagamento',
            new_name='metodo_do_pagamento',
        ),
    ]
