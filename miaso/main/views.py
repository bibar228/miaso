from django.shortcuts import render
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action, api_view

from drf_yasg.utils import swagger_auto_schema
from main.models import Copch, Poly, Cold
from main.serializers import CopchSerializer, PolySerializer, ColdSerializer
from rest_framework.response import Response



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





