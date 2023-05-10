from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.routers import SimpleRouter, Route

from main.models import Copch, Poly, Cold
from main.serializers import CopchSerializer, PolySerializer, ColdSerializer



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


class CustomReadOnlyRouter(SimpleRouter):
    """
    A router for read-only APIs, which doesn't use trailing slashes.
    """
    routes = [Route(url=r'{prefix}', mapping={'get': 'list'}, name='{basename}-list', detail=False, initkwargs={'suffix': 'List'})]


router_main = CustomReadOnlyRouter()

router_main.register(r"copch", CopchViewSet)
router_main.register(r"poly", PolyViewSet)
router_main.register(r"cold", ColdViewSet)
