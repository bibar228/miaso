from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import AnonymousUser
from django.db.models import Count
from django.http import HttpResponse
from django.shortcuts import render

from rest_framework import viewsets, permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from basket.forms import OrderCreateForm
from basket.models import OrderItem, Order
from basket.serializers import OrderSerializer, PostOrderSerializer


class OrderView(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = OrderSerializer


    def get_queryset(self):

        if self.request.user:
            user_orders = OrderItem.objects.filter(user=self.request.user).select_related("order")
            return user_orders
        else:
            return "Вам необходимо авторизоваться"


def order_create(request):
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in request.POST:
                OrderItem.objects.create(order=order,
                                         copch_product=item['product'],
                                         cold_product=item["cold_product"],
                                         poly_product=item["poly_product"],
                                         price=item['price'],
                                         quantity=item['quantity'])

            return request
