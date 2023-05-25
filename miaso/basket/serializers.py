from django.core.validators import RegexValidator
from rest_framework import serializers

from basket.models import OrderItem, Order
from users.models import User, AuthtokenToken


class OrderSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.email')
    product = serializers.CharField(source='product.name')

    class Meta:
        model = OrderItem
        # Назначаем поля которые будем использовать
        fields = ["user", "order_id", "product", "price", "quantity"]


class CreateOrderSerializer(serializers.Serializer):
    first_name = serializers.CharField()
    token_user = serializers.CharField()
    address = serializers.CharField()
    phone = serializers.CharField()
    comment = serializers.CharField()

    #user = AuthtokenToken.objects.values().filter(key=user)
    class Meta:
        model = Order
        # Назначаем поля которые будем использовать
        fields = ["first_name", "token_user", "address", "phone", "comment"]

    def save(self, *args, **kwargs):
        user_number = AuthtokenToken.objects.filter(key=self.validated_data["token_user"]).get().user_id
        user_name = User.objects.filter(id=user_number).get().email

        order = Order(
            first_name=self.validated_data['first_name'],
            user=user_name,
            address=self.validated_data["address"],
            phone=self.validated_data["phone"],
            comment=self.validated_data["comment"]
        )

        order.save()
        return order

#order = serializers.CharField()
#    copch_product = serializers.CharField()
#    cold_product = serializers.CharField()
 #   poly_product = serializers.CharField()
#    price = serializers.DecimalField(max_digits=10, decimal_places=2)
 #   quantity = serializers.DecimalField(max_digits=10, decimal_places=3, default=1)