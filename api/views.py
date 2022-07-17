from django.shortcuts import render

from django.db.models import F, Q, Sum
from .models import Revendedor
from .serializers import RevendedorSerializer

from rest_framework import serializers
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet

# Create your views here.
class RevendedorViewSet(ReadOnlyModelViewSet):
    model = Revendedor
    serializer_class = RevendedorSerializer
    queryset = Revendedor.objects.all()