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

from basket.models import OrderItem
from basket.serializers import OrderSerializer, PostOrderSerializer


class OrderView(viewsets.ModelViewSet):

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = OrderSerializer


    def get_queryset(self):
        user_orders = OrderItem.objects.filter(user=self.request.user).select_related("order")
        return user_orders


class PostOrderView(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = PostOrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(self.request.user)
        else:
            data = serializer.errors
            return Response(data)