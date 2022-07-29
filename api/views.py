from django.shortcuts import render

from .models import Avaria, Carro, Doc_Carro, Doc_Revendedor, Revendedor, Visita
from .serializers import AvariaSerializer, CarroSerializer, DocCarroSerializer, DocRevendedorSerializer, RevendedorSerializer, VisitaSerializer

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.generics import get_object_or_404

# Create your views here.
class RevendedorViewSet(viewsets.ModelViewSet):
    serializer_class = RevendedorSerializer
    queryset = Revendedor.objects.all()

    @action(detail=False, methods=['get'])
    def documentos(self, request, pk=None):
        documentos = Doc_Revendedor.objects.all()
        serializer = DocRevendedorSerializer(documentos, many=True)
        return Response(serializer.data)


class CarroViewSet(viewsets.ModelViewSet):
    serializer_class = CarroSerializer
    queryset = Carro.objects.all()

    @action(detail=False, methods=['get'])
    def documentos(self, request, pk=None):
        documentos = Doc_Carro.objects.all()
        serializer = DocCarroSerializer(documentos, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def visitas(self, request, pk=None):
        visitas = Visita.objects.all()
        serializer = VisitaSerializer(visitas, many=True)
        return Response(serializer.data)


class AvariaViewSet(viewsets.ModelViewSet):
    serializer_class = AvariaSerializer
    queryset = Avaria.objects.all()


class VisitaViewSet(viewsets.ModelViewSet):
    serializer_class = VisitaSerializer
    queryset = Visita.objects.all()
