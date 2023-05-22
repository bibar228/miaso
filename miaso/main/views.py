from django.shortcuts import render
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action, api_view

from drf_yasg.utils import swagger_auto_schema

from rest_framework.response import Response

from main.models import Product
from main.serializers import ProductSerializer


# Create your views here.
class CopchViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.filter(category=1)
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ProductSerializer


class PolyViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.filter(category=2)
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ProductSerializer


class ColdViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.filter(category=3)
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ProductSerializer




