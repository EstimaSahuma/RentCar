from pyexpat import model
from rest_framework import serializers

from .models import Avaria, Avatar_Carro, Carro, Doc, Doc_Carro, Doc_Revendedor, Revendedor, User_Revendedor, Visita

class RevendedorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Revendedor
        fields = ('name', 'phone_primary', 'phone_secondary', 'email', 'bi', 'avatar')


class CarroSerializer(serializers.ModelSerializer):

    class Meta:
        model = Carro
        fields = ('marca', 'cor', 'matricula', 'modelo', 'tipo_motor', 'estado')


class AvariaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Avaria
        fields = ('carro', 'designacao', 'descricao')


class AvatarCarroSerializer(serializers.ModelSerializer):

    class Meta:
        model = Avatar_Carro
        fields = ('carro', 'designacao', 'descricao')


class VisitaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Visita
        fields = ('carro', 'nome', 'phone_primary', 'phone_secondary', 'data_visita')


class UserRevendedorSerializer(serializers.ModelSerializer):

    class Meta:
        model = User_Revendedor
        fields = ('user', 'revendedor')


class DocRevendedorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Doc_Revendedor
        fields = ('revendedor')


class DocCarroSerializer(serializers.ModelSerializer):

    class Meta:
        model = Doc_Carro
        fields = ('carro')