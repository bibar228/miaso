from django.core.validators import RegexValidator
from rest_framework import serializers

from basket.models import OrderItem, Order
from users.models import User, AuthtokenToken


class OrderItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderItem
        fields = ["user", "order", "product", "price", "quantity"]

    def save(self, *args, **kwargs):

        order = OrderItem(
            user=self.validated_data['user'],
            order=self.validated_data['order'],
            product=self.validated_data["product"],
            price=self.validated_data["price"],
            quantity=self.validated_data["quantity"]
        )

        order.save()
        return order


class CreateOrderSerializer(serializers.Serializer):
    first_name = serializers.CharField()
    token_user = serializers.CharField()
    address = serializers.CharField()
    phoneNumberRegex = RegexValidator(regex=r"^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{11}$")
    phone = serializers.CharField(validators=[phoneNumberRegex], max_length=11)
    comment = serializers.CharField()


    class Meta:
        model = Order
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