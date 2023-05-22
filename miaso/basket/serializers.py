from rest_framework import serializers

from basket.models import OrderItem, Order
from users.models import User


class OrderSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.email')
    product = serializers.CharField(source='product.name')

    class Meta:
        model = OrderItem
        # Назначаем поля которые будем использовать
        fields = ["user", "order_id", "product", "price", "quantity"]


class PostOrderSerializer(serializers.Serializer):

    user = serializers.CharField()
    class Meta:
        model = Order
        # Назначаем поля которые будем использовать
        fields = ["user", "order_id", "product", "price", "quantity"]

    def save(self, *args, **kwargs):
        # Создаём объект класса User
        user = Order(
            user=self.validated_data['user'],  # Назначаем Email

        )
        # Сохраняем пользователя
        user.save()


#order = serializers.CharField()
#    copch_product = serializers.CharField()
#    cold_product = serializers.CharField()
 #   poly_product = serializers.CharField()
#    price = serializers.DecimalField(max_digits=10, decimal_places=2)
 #   quantity = serializers.DecimalField(max_digits=10, decimal_places=3, default=1)