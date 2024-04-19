from rest_framework import serializers
from app.models import Verduras, Frutas, Entrega, Pagamento, Item

class VerdurasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Verduras # variaveis de produto adicionar colchetes no lugar de "all" TODOS
        fields = ['nome_do_produto', 'preco_individual', 'quantidade_disponivel' ]

class FrutasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Frutas #variaveis de produto
        fields = ['nome_do_produto', 'preco_individual', 'quantidade_disponivel'] 

class EntregaSerializer(serializers.ModelSerializer):
    itens = serializers.PrimaryKeyRelatedField(many=True, queryset=Item.objects.all())
    pagamento = serializers.PrimaryKeyRelatedField(queryset=Pagamento.objects.all())

    class Meta:
        model = Entrega
        fields = ['nome_do_cliente', 'endereco_da_entrega', 'data_da_entrega', 'pagamento', 'itens']

class PagamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pagamento
        fields = ['metodo_do_pagamento', 'valor_total']

class ItemSerializer(serializers.ModelSerializer):
    entrega = serializers.PrimaryKeyRelatedField(queryset=Entrega.objects.all())

    class Meta:
        model = Item
        fields = ['entrega', 'nome_do_produto', 'quantidade', 'preco_individual_item']
