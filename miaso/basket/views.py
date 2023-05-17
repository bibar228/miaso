from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import AnonymousUser
from django.db.models import Count
from django.http import HttpResponse
from django.shortcuts import render

from rest_framework import viewsets, permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from basket.models import OrderItem
from basket.serializers import OrderSerializer


class OrderView(viewsets.ModelViewSet):

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = OrderSerializer


    def get_queryset(self):
        user_orders = OrderItem.objects.filter(user=self.request.user)
        return user_orders
