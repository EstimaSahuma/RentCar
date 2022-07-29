from pyexpat import model
from rest_framework import serializers

from .models import Avaria, Avatar_Carro, Carro, Doc, Doc_Carro, Doc_Revendedor, Revendedor, User_Revendedor, Visita




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
        fields = ('revendedor', 'designation', 'description', 'avatar')


class DocCarroSerializer(serializers.ModelSerializer):

    class Meta:
        model = Doc_Carro
        fields = ('carro', 'designation', 'description', 'avatar')


class RevendedorSerializer(serializers.ModelSerializer):
    doc_revendedores = DocRevendedorSerializer(many=True, read_only=True)

    class Meta:
        model = Revendedor
        fields = ('name', 'phone_primary', 'phone_secondary', 'email', 'bi', 'avatar', 'doc_revendedores')


class CarroSerializer(serializers.ModelSerializer):
    doc_carros = DocCarroSerializer(many=True, read_only=True)
    avarias = AvariaSerializer(many=True, read_only=True)
    avatar_carroes = AvatarCarroSerializer(many=True, read_only=True)
    visitas = VisitaSerializer(many=True, read_only=True)
    class Meta:
        model = Carro
        fields = ('marca', 'cor', 'matricula', 'modelo', 'tipo_motor', 'estado',
                 'doc_carros', 'avarias', 'avatar_carroes', 'visitas')
