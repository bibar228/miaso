from rest_framework import serializers

from basket.models import OrderItem


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        # Поля модели которые будем использовать
        model = OrderItem
        # Назначаем поля которые будем использовать
        fields = "__all__"