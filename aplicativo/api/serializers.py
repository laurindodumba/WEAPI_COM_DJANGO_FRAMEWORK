from rest_framework import serializers

from aplicativo import models

#Criar a classe dos carros

from rest_framework import serializers
from aplicativo.models import Carro

class CarrosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carro
        fields = ['id', 'name', 'cor', 'ano', 'cidade', 'estado', 'capacidade']

    def create(self, validated_data):
        """
        Cria e retorna uma nova instância de Carro com os dados validados.
        """
        return Carro.objects.create(**validated_data)
