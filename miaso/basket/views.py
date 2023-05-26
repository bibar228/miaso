import json

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import AnonymousUser
from django.db.models import Count
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.renderers import JSONRenderer

from rest_framework import viewsets, permissions, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from basket.forms import OrderCreateForm
from basket.models import OrderItem, Order
from basket.serializers import CreateOrderSerializer, OrderItemSerializer
from users.models import AuthtokenToken


class OrderView(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = OrderItemSerializer

    def get_queryset(self):

        if self.request.user:
            user_orders = OrderItem.objects.filter(user=self.request.user)
            return user_orders
        else:
            return "Вам необходимо авторизоваться"

class Token_User(viewsets.ModelViewSet):
    def get_queryset(self):
        user = AuthtokenToken.objects.filter(user=self.request.user)
        return user

from rest_framework.test import APIRequestFactory

class CreateOrderView(CreateAPIView):
    # Добавляем serializer UserRegistrSerializer
    serializer_class = CreateOrderSerializer
    # Добавляем права доступа
    permission_classes = [IsAuthenticated]
    def post(self, request, *args, **kwargs):

        serializer = CreateOrderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        order_number = Order.objects.first()
        return HttpResponse(order_number, status=status.HTTP_201_CREATED)


class CreateOrderItemView(CreateAPIView):
    # Добавляем serializer UserRegistrSerializer
    serializer_class = OrderItemSerializer
    # Добавляем права доступа
    permission_classes = [IsAuthenticated]
    def post(self, request, *args, **kwargs):

        serializer = CreateOrderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return HttpResponse("success", status=status.HTTP_201_CREATED)

