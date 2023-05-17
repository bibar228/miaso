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


#class OrderView(viewsets.ModelViewSet):
#    queryset = OrderItem.objects.all()
#    authentication_classes = (TokenAuthentication,)
#    permission_classes = (IsAuthenticated,)
#    serializer_class = OrderSerializer

 #   def get(self, request):
#       user_orders = OrderItem.objects.filter(user=re  quest.user)
 #       return HttpResponse(user_orders)

def order_view(request):
    user_orders = OrderItem.objects.filter(user=request.user.id).values()
    return HttpResponse(user_orders)
