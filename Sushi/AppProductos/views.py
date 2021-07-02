from django.http import response
from django.shortcuts import render
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ProductoSerializer, TipoSerializer
from .models import Producto, Tipo
from rest_framework import viewsets
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test

# Create your views here.
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class TipoViewSet(viewsets.ModelViewSet):
    queryset = Tipo.objects.all()
    serializer_class = TipoSerializer