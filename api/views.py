from django.shortcuts import render

from django.db.models import F, Q, Sum
from .models import Revendedor
from .serializers import RevendedorSerializer

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework import generics
from rest_framework.generics import get_object_or_404

# Create your views here.
class RevendedorViewSet(generics.ModelViewSet):
    serializer_class = RevendedorSerializer
    queryset = Revendedor.objects.all()

    