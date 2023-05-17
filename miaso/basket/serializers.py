from rest_framework import serializers

from basket.models import OrderItem


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        # Поля модели которые будем использовать
        model = OrderItem
        # Назначаем поля которые будем использовать
        fields = ["user_id", "order_id", "copch_product_id", "cold_product_id", "poly_product_id", "price", "quantity"]