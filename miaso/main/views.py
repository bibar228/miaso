from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.decorators import action

from .models import Copch, Poly, Cold
from .serializers import CopchSerializer, PolySerializer, ColdSerializer



# Create your views here.
class CopchViewSet(viewsets.ModelViewSet):
    queryset = Copch.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CopchSerializer


class PolyViewSet(viewsets.ModelViewSet):
    queryset = Poly.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = PolySerializer


class ColdViewSet(viewsets.ModelViewSet):
    queryset = Cold.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ColdSerializer

