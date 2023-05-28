
from django.http import HttpResponse


from rest_framework import viewsets, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from basket.models import OrderItem, Order
from basket.serializers import CreateOrderSerializer, OrderItemSerializer
from main.models import Product
from users.models import AuthtokenToken
import telebot

telega_token = "5926919919:AAFCHFocMt_pdnlAgDo-13wLe4h_tHO0-GE"

class OrderView(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = OrderItemSerializer

    def get_queryset(self):
    #получение всех заказов юзера за все время
        if self.request.user:
            user_orders = OrderItem.objects.filter(user=self.request.user)
            return user_orders
        else:
            return "Вам необходимо авторизоваться"



class CreateOrderView(CreateAPIView):

    serializer_class = CreateOrderSerializer
    permission_classes = [IsAuthenticated]
    def post(self, request, *args, **kwargs):
        #создание номера заказа с характеристиками
        serializer = CreateOrderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        order_number = Order.objects.first()
        return HttpResponse(order_number, status=status.HTTP_201_CREATED)




class CreateOrderItemView(CreateAPIView):
    #создание итемов заказа с продуктами и отрпавка заказа в телегу
    serializer_class = OrderItemSerializer
    permission_classes = [IsAuthenticated]
    def post(self, request, *args, **kwargs):
        character_order = []
        for i in request.data:
            serializer = OrderItemSerializer(data=i)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            character_order.append(f"{Product.objects.get(id=i['product']).name}, Количество - {i['quantity']}кг., Ориентировочная цена - {i['price']} руб.")


        chat_id = -695765690
        bot = telebot.TeleBot(telega_token)
        user_orders = Order.objects.get(id=request.data[0]["order"])
        message = f"{user_orders}\nИмя - {user_orders.first_name}\nАдресс - {user_orders.address}\nТелефон - {user_orders.phone}\nКомментарий к заказу - {user_orders.comment}"
        message += "\n\nСостав заказа:"
        for i in range(len(character_order)):
            message += f"\n{str(i+1)}. {character_order[i]}"
        bot.send_message(chat_id, message)
        return HttpResponse("Success orderitem")

